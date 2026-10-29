# SEO & Go-Live Plan — kiavipromocode.com

Prepared October 29, 2026, from live DataForSEO pulls (see `SPEC.md` for the full keyword analysis and the promo-vs-discount decision). This is the launch sequence and the measurement plan.

## Strategy in one paragraph

Unlike gustodiscountcode.com, the namesake phrase here has **zero search volume** — nobody searches "kiavi promo code" yet. So the site doesn't wait for code searches: it targets the real Kiavi demand (~5,000/mo of reviews, hard-money, product, requirements, and comparison long-tail, almost all KD 0–12) with genuinely useful pages, and converts that traffic with the $350 new-customer bonus on every page. The domain owns the code phrase for free in case Kiavi's consumer awareness ever creates volume — on day one we will be the only site on earth targeting it.

## Phase 0 — before launch (blockers)

1. **Read Kiavi's affiliate T&Cs** (kiavi.com/affiliateprogramtermsandconditions) and confirm brand-in-domain is allowed. This is the only step that could change the domain choice.
2. **Buy domains:** `kiavipromocode.com` (primary) + `kiavidiscountcode.com` (defensive, 301 to primary). ~$20/yr total.
3. **Verify the affiliate link is live** — `try.kiavi.com/z51bru4xa2o2` currently redirects to Kiavi signup correctly (checked Oct 29). Confirm attribution shows in the PartnerStack dashboard with a test click.
4. **Add `kiavipromocode.com` to Plausible** at analytics.loopdash.com (snippet already in the layout).

## Phase 1 — launch week

1. **Deploy.** Repo auto-deploys to GitHub Pages on push to `main` (`.github/workflows/deploy.yml`). Point the apex + www DNS at Pages, set the custom domain, enforce HTTPS. (Note: free GitHub Pages requires a public repo — either flip visibility or deploy to Cloudflare Pages instead; the build is plain `npm run build` → `_site/` either way.)
5. **Search Console from day one** (the Gusto site's biggest regret was no API access and late GSC data): verify the domain property, submit `sitemap.xml`, and request indexing on the 6 money pages (/, review, rates, requirements, /kiavi-vs/, calculator).
6. **Bing Webmaster Tools** — import from GSC, one click, free conversions from investor demographics.
7. **Baseline snapshot:** re-run a DataForSEO `ranked_keywords` pull against `kiavipromocode.com` the day of launch (expect ~0) and archive it — same discipline as the Gusto `tasks/seo_pull.py` workflow. Port that script to this repo with `TARGET = "kiavipromocode.com"`.

## Phase 2 — first 60 days (indexation + links)

1. **Internal-link audit after first crawl** — every page already cross-links; confirm no orphans in GSC's page report.
2. **Minimum viable backlinks.** A brand-new domain needs a handful of real links to get crawled seriously:
   - Link from loopdash.com and any sibling property where relevant.
   - BiggerPockets forum profile + genuinely helpful answers on Kiavi threads (there are many "is Kiavi legit" threads — our FAQ is the canonical answer).
   - HARO/Featured-style quotes on hard-money topics.
   - Do NOT buy links; a YMYL microsite on a fresh domain can't absorb that risk.
3. **Watch the review cluster first.** `kiavi review` (880, KD 3) is the highest-volume winnable term; expect first movement in weeks 3–8.
4. **Ship the seo_pull.py port** and set a recurring 2-week re-pull cadence (same rhythm as the Gusto site).

## Phase 3 — compounding (60+ days)

1. **Expand comparisons** as data shows which "kiavi vs X" phrases get impressions in GSC (candidates: AMZA Capital, Easy Street Capital, Dominion Financial, LendingOne, Visio). One JSON entry per competitor.
2. **Expand FAQs from GSC queries** — the Gusto playbook: per-question pages with FAQPage schema became the site's top traffic pages. Mine GSC's query report monthly for new questions.
3. **State pages (only if data supports):** `kiavi-[state]` hard-money pages if GSC shows geo-modified queries. Don't pre-build 50 thin pages.
4. **Quarterly fact audit:** rates ranges, the $350 figure, state coverage (Utah), product lineup (new construction launched 2025 — things change). Stale YMYL facts are a ranking and trust liability.

## Measurement

- **Rankings:** DataForSEO ranked_keywords pull every 2 weeks (~$0.08/pull). Baseline tracked set: kiavi review, kiavi reviews, is kiavi legit, kiavi rates, kiavi requirements, kiavi credit score requirements, kiavi minimum loan amount, kiavi dscr loan, kiavi bridge loan, kiavi fix and flip, kiavi hard money lender, kiavi competitors, kiavi arv calculator, kiavi phone number, kiavi payoff request, kiavi promo code, kiavi discount code.
- **Traffic & conversions:** Plausible — outbound-link goal on `try.kiavi.com` clicks (set up the goal day one; the Gusto site added goals late and lost the early funnel picture).
- **Revenue:** PartnerStack dashboard (signups → closed loans). A closed loan pays out on Kiavi's cycle, so expect a 1–3 month lag between click and commission.
- **Success criteria:** 90 days — indexed on all pages, top-20 on 3+ review/requirements terms, first affiliate signup. 180 days — top-10 on `kiavi review`, 500+ organic visits/mo, first closed-loan commission.

## What we deliberately did differently from the Gusto launch

| Gusto lesson | Applied here |
|---|---|
| robots.txt shipped without sitemap declaration | Declared day one |
| No GSC API / late Search Console setup | GSC + Bing in launch week, domain property |
| Plausible goals configured late | Outbound-click goal at launch |
| FAQ content changes needed Rails data migrations | Static JSON — edit, commit, deploy |
| Scheduler/cron never configured for reports | Static site; re-pull is a local script on a calendar reminder |
| Code-phrase volume carried the site | No code-phrase volume exists; cluster content carries it |
