(function () {
  var LTC_MAX = 0.95;      // Kiavi max loan-to-cost
  var ARV_MAX = 0.80;      // Kiavi max loan vs after-repair value
  var POINTS = 0.02;       // assumed origination points
  var SELL_COSTS = 0.08;   // agent + closing + concessions on exit

  var $ = function (id) { return document.getElementById(id); };
  var fmt = function (n) {
    return "$" + Math.round(n).toLocaleString("en-US");
  };

  function row(label, value, cls) {
    return '<div><span>' + label + '</span><span class="num ' + (cls || "") + '">' + value + "</span></div>";
  }

  function calc() {
    var purchase = +$("purchase").value || 0;
    var rehab = +$("rehab").value || 0;
    var arv = +$("arv").value || 0;
    var months = Math.min(Math.max(+$("months").value || 12, 1), 24);
    var rate = (+$("rate").value || 0) / 100;

    var totalCost = purchase + rehab;
    var ltcCeiling = totalCost * LTC_MAX;
    var arvCeiling = arv * ARV_MAX;
    var loan = Math.min(ltcCeiling, arvCeiling);
    var binding = ltcCeiling <= arvCeiling ? "95% LTC" : "80% ARV";

    var points = loan * POINTS;
    var cashToClose = totalCost - loan + points;
    var interest = loan * rate * (months / 12);
    var sellCosts = arv * SELL_COSTS;
    var profit = arv - totalCost - points - interest - sellCosts;

    var maxOffer70 = arv * 0.7 - rehab;
    var overRule = purchase > maxOffer70;

    var html = "";
    html += row("Max Kiavi loan (binds at " + binding + ")", fmt(loan));
    html += row("Estimated cash to close (gap + " + (POINTS * 100) + " pts)", fmt(cashToClose), cashToClose > totalCost * 0.3 ? "neg" : "");
    html += row("Interest over " + months + " months", fmt(interest));
    html += row("Selling costs at exit (~" + SELL_COSTS * 100 + "%)", fmt(sellCosts));
    html += row("70% rule max offer", fmt(maxOffer70), overRule ? "neg" : "");
    if (overRule) {
      html += row("70% rule check", "Offer exceeds the rule by " + fmt(purchase - maxOffer70), "neg");
    }
    html += row("Projected profit", fmt(profit), profit < 0 ? "neg" : "");
    html += row("Profit if ARV comes in 10% low", fmt(profit - arv * 0.1), profit - arv * 0.1 < 0 ? "neg" : "");

    $("results").innerHTML = html;
  }

  ["purchase", "rehab", "arv", "months", "rate"].forEach(function (id) {
    $(id).addEventListener("input", calc);
  });
  calc();
})();
