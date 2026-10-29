# Spec — kiavipromocode.com

Prepared October 29, 2026. Keyword data pulled live from DataForSEO (Labs + Google Ads endpoints, US / English / Google); raw exports archived in the gusto workspace at `.context/seo-kiavi/`. Research cost: ~$0.26.

## What this is

A static affiliate microsite for Kiavi (the largest US fix-and-flip lender, formerly LendingHome), modeled on gustodiscountcode.com but built on Eleventy instead of Rails. It monetizes one link — the Kiavi affiliate referral `https://try.kiavi.com/z51bru4xa2o2` — which pays the site a commission per closed loan and pays the referred borrower **$350 cash after their first qualified closing** (verified on kiavi.com/affiliates and kiavi.com/refer, Oct 29, 2026).

## The keyword decision: promo code vs. discount code

**Answer: "kiavi promo code" — but neither phrase has measurable volume today, and that reshapes the whole strategy.**

What the data showed (DataForSEO, Oct 29, 2026):

- **Every code/coupon variation is a zero.** `kiavi promo code`, `kiavi discount code`, `kiavi coupon (code)`, `kiavi referral (code/program)`, `kiavi promo`, `kiavi discount`, `kiavi bonus`, `kiavi sign up bonus` — all returned no recorded volume in both DataForSEO Labs *and* Google Ads search-volume endpoints. The live SERP for "kiavi promo code" contains zero coupon sites — nobody targets it because nobody searches it.
- **Why: lending isn't couponable.** A proxy pull across fintech/lending brands confirms the category pattern — Chime (consumer fintech): promo 6,600 / coupon 6,600 / discount 0; but lenders: Rocket Mortgage promo 10, LendingClub 10, Groundfloor 10, Fund That Flip 0, Lima One 0. People coupon-hunt apps, not loans.
- **Tiebreak for the domain:** across every brand tested, "promo code" ≥ "discount code" (discount never wins a single matchup). If Kiavi's consumer awareness grows, the volume shows up on "promo code" first.
- **Where Kiavi demand actually is** (Labs, US):

| Cluster | Keywords | Volume | KD |
|---|---|---|---|
| Brand head | kiavi | 12,100 | 12 |
| Navigational | kiavi login (1,000), dashboard login (70), sign in (70), broker login (50) | ~1,190 | 4–15 |
| **Reviews** | kiavi review/reviews (880+880 shared), funding reviews (90), loan(s) reviews (80), lending reviews (30), is kiavi legit (40) | ~1,100 | 0–5 |
| **Hard money** | kiavi hard money lender/lenders/lending (590×3), hard money (110), hard money loan(s) (220) | ~1,990 | 0–23 |
| Company/brand | kiavi funding (880), funding inc (390), lending (480), lender (140), mortgage (90) | ~1,980 | 0–11 |
| **Products** | dscr loan (210) + requirements (30), bridge loan (110), fix-and-flip variants (200), loan/loans (640) | ~1,190 | 0–8 |
| **Tools** | arv estimator (140), arv calculator (90) | 230 | 2–10 |
| **Requirements/ops** | requirements (40), loan requirements (40), credit score requirements (30+20), minimum loan amount (40), rates (40), payoff (30+30) | ~270 | 0–1 |
| Contact | phone number (140, $35 CPC), customer service (50+40) | 230 | 0–5 |
| Competitive | kiavi competitors (50) | 50 | 0 |

**Strategic conclusion:** the domain/brand is `kiavipromocode.com` (portfolio consistency with gustodiscountcode.com, owns the phrase if volume ever materializes, zero competition on it), but **the traffic plan is the review/rates/requirements/comparison content**, with the $350 bonus as the conversion layer on every page. This is the inverse of the Gusto site, where the code phrase itself carried volume.

Domains checked Oct 29 — all available: kiavipromocode.com (primary), kiavidiscountcode.com (buy as defensive 301), kiavicode.com, kiavidiscount.com, kiavipromo.com (optional).

## The honest-broker positioning

Kiavi issues no coupon codes. The site says so in the first screen — "the promo code is a link, not a code" — and documents the real $350 new-customer bonus. This honesty is the moat: every page that ranks earns trust by being the only accurate answer, and the FTC-required affiliate disclosure doubles as credibility.

## Site architecture (all built)

| URL | Target keywords | Notes |
|---|---|---|
| `/` | kiavi promo code, discount code, coupon, bonus | Offer mechanics + hub links |
| `/kiavi-review/` | kiavi review(s) ~1,100/mo KD ≤5 | Article schema; honest pros/cons |
| `/kiavi-rates/` | kiavi rates, pricing levers | |
| `/kiavi-requirements/` | requirements, credit score, minimums | |
| `/kiavi-dscr-loans/` | kiavi dscr loan (210) + requirements | |
| `/kiavi-fix-and-flip/` | fix-and-flip variants, bridge loan (~310) | |
| `/kiavi-deal-calculator/` | arv calculator/estimator adjacency (230) | Interactive JS calculator (95% LTC / 80% ARV / 70% rule) |
| `/kiavi-vs/` | kiavi competitors (50, KD 0) | ItemList schema comparison chart |
| `/kiavi-vs/{groundfloor,lima-one-capital,rcn-capital,upright,new-silver}/` | "[lender] vs kiavi" long-tail | Generated from `competitors.json` — the Gusto KD-0 comparison playbook |
| `/faqs/` + 13 per-FAQ pages | is kiavi legit, minimum loan, credit score, phone number, payoff request, states, who owns, income verification, close speed, ARV estimator, broker program, prepayment penalty, how the $350 works | FAQPage schema on index and each page — per-FAQ pages are the proven Gusto traffic engine |
| `/disclosure/`, `/privacy/`, `/404.html` | — | FTC compliance; trust |

Content rules learned from the Gusto site: pages must be genuinely useful, not thin (the generalist aggregators we're outranking are thin); every page gets one inline CTA + the footer CTA band; facts that change (rates) are framed as ranges with "get the live quote" CTAs; comparisons admit where Kiavi loses.

## Stack

- **Eleventy 3.x** (ESM config), Nunjucks templates, no client framework. Comparisons and FAQs generate from JSON data files (`src/_data/competitors.json`, `faqs.json`) via pagination — adding a competitor or FAQ is one JSON entry, same pattern as the Gusto `payroll_comparison.rb`.
- **SEO plumbing:** canonical, OG, per-page JSON-LD (WebSite, Article, FAQPage, ItemList, WebApplication, BreadcrumbList via crumbs), `sitemap.xml` generated from collections, `robots.txt` with sitemap declaration (day-one this time).
- **Analytics:** Plausible snippet pointed at `analytics.loopdash.com`, domain `kiavipromocode.com`. Add the site in Plausible before launch.
- **Affiliate links:** `rel="sponsored noopener"`, target `_blank`, single source of truth in `src/_data/site.json` (`affiliateLink`, `offerAmount`) — if PartnerStack reissues the link or Kiavi changes the bonus, it's a one-line change.
- **Hosting:** GitHub Pages via Actions workflow (`.github/workflows/deploy.yml`). Free, no server, no Heroku dyno. Cloudflare Pages is the drop-in alternative if we want the repo to stay private on a free plan.

## Risks

- **Trademark/brand-bidding:** the domain contains "Kiavi." Kiavi runs an official affiliate program, which implies tolerance for affiliate sites, but PartnerStack affiliate terms commonly prohibit *paid search* brand bidding and sometimes brand-in-domain. **Read Kiavi's affiliate T&Cs (kiavi.com/affiliateprogramtermsandconditions) before buying the domain**; if brand-in-domain is prohibited, fall back to an investor-brand domain and keep the same content.
- **Zero-volume head term:** the site's namesake phrase may never get searches. Mitigated by the cluster strategy above — the domain is branding, not the plan.
- **YMYL content:** lending content is held to a higher E-E-A-T bar. Mitigations shipped: full disclosure page, NMLS numbers cited, no advice framing, ranges instead of stale precise rates.
- **Offer drift:** the $350 figure is Kiavi's to change. `offerAmount` lives in one data file; verify quarterly.

## Go-live checklist

See `SEO_PLAN.md` for the full launch sequence and measurement plan.
