#!/usr/bin/env python3
"""
Re-pull DataForSEO rankings for kiavipromocode.com and diff against the
tracked-keyword baseline from SEO_PLAN.md (site launched with zero rankings;
the launch-day pull is the baseline).

Credentials come from the environment; read them from 1Password or Heroku:

    DATAFORSEO_LOGIN=$(op read "op://loopdash-ops/dataforseo-api/username") \
    DATAFORSEO_PASSWORD=$(op read "op://loopdash-ops/dataforseo-api/password") \
    python3 tasks/seo_pull.py

    # or, when 1Password is signed out:
    DATAFORSEO_LOGIN=$(heroku config:get DATAFORSEO_LOGIN -a gusto-discount-code) \
    DATAFORSEO_PASSWORD=$(heroku config:get DATAFORSEO_PASSWORD -a gusto-discount-code) \
    python3 tasks/seo_pull.py

Raw exports are written to .context/seo/ (gitignored). US / English / google,
matching the October 29, 2026 research pull archived in research/.
"""
import base64
import json
import os
import sys
import urllib.request
from pathlib import Path

TARGET = "kiavipromocode.com"
LOCATION_CODE = 2840  # United States
LANGUAGE_CODE = "en"
OUT_DIR = Path(__file__).resolve().parent.parent / ".context" / "seo"

# Tracked set from SEO_PLAN.md. Baseline is "unranked" (site launched Oct 2026).
TRACKED = [
    "kiavi review",
    "kiavi reviews",
    "is kiavi legit",
    "kiavi rates",
    "kiavi requirements",
    "kiavi credit score requirements",
    "kiavi minimum loan amount",
    "kiavi dscr loan",
    "kiavi bridge loan",
    "kiavi fix and flip",
    "kiavi hard money lender",
    "kiavi competitors",
    "kiavi arv calculator",
    "kiavi phone number",
    "kiavi payoff request",
    "kiavi promo code",
    "kiavi discount code",
]


def call(path, payload):
    login = os.environ["DATAFORSEO_LOGIN"]
    password = os.environ["DATAFORSEO_PASSWORD"]
    token = base64.b64encode(f"{login}:{password}".encode()).decode()
    req = urllib.request.Request(
        f"https://api.dataforseo.com{path}",
        data=json.dumps([payload]).encode(),
        headers={
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Pulling ranked_keywords ...", file=sys.stderr)
    ranked = call(
        "/v3/dataforseo_labs/google/ranked_keywords/live",
        {
            "target": TARGET,
            "location_code": LOCATION_CODE,
            "language_code": LANGUAGE_CODE,
            "limit": 1000,
            "order_by": ["ranked_serp_element.serp_item.rank_group,asc"],
        },
    )
    (OUT_DIR / "ranked_keywords.json").write_text(json.dumps(ranked, indent=2))

    cost = ranked.get("cost", 0)
    items = (ranked["tasks"][0]["result"] or [{}])[0].get("items") or []
    current = {}
    for it in items:
        kw = it["keyword_data"]["keyword"]
        pos = it["ranked_serp_element"]["serp_item"]["rank_group"]
        vol = (it["keyword_data"].get("keyword_info") or {}).get("search_volume")
        if kw not in current or pos < current[kw][0]:
            current[kw] = (pos, vol)

    print(f"\n{TARGET}: {len(current)} ranked keywords (cost ${cost:.2f})\n")
    print(f"{'keyword':42s} {'pos':>5s} {'vol':>7s}")
    for kw in TRACKED:
        pos, vol = current.get(kw, ("-", "-"))
        print(f"{kw:42s} {str(pos):>5s} {str(vol):>7s}")

    extras = sorted(
        (k for k in current if k not in TRACKED),
        key=lambda k: current[k][0],
    )[:25]
    if extras:
        print("\nBest untracked rankings:")
        for kw in extras:
            pos, vol = current[kw]
            print(f"{kw:42s} {str(pos):>5s} {str(vol):>7s}")


if __name__ == "__main__":
    main()
