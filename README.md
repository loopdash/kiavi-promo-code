# kiavipromocode.com

Static affiliate microsite for Kiavi's $350 new-customer bonus, built with [Eleventy](https://www.11ty.dev/). Sister site to [gustodiscountcode.com](https://github.com/loopdash/gusto-discount-code).

- **Spec & keyword research:** [SPEC.md](SPEC.md)
- **Launch & SEO plan:** [SEO_PLAN.md](SEO_PLAN.md)

## Develop

```bash
npm install
npm start          # dev server at localhost:8080
npm run build      # output to _site/
```

## Editing content

- **Affiliate link / offer amount:** `src/_data/site.json` — single source of truth.
- **FAQs:** add an entry to `src/_data/faqs.json`; the index listing, per-question page, and FAQPage schema generate automatically.
- **Competitor comparisons:** add an entry to `src/_data/competitors.json`; the chart row and head-to-head page generate automatically.
- **Pages:** `src/*.njk`.

## Deploy

Pushes to `main` build and deploy via GitHub Pages (`.github/workflows/deploy.yml`). Custom domain + DNS setup is covered in SEO_PLAN.md Phase 1.
