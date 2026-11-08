# Piracy Site Tracker — Offline Public Map + Private Research Tier

This package is a local, file-based research tracker compiled from the supplied brief. It separates a private research CSV from a redacted public CSV and provides an offline public map at `map/index.html`.

## Safety and scope

- The public map displays **names, categories, and statuses only**.
- It contains no live links, no click-through access, no domain list, and no private notes.
- The animation is procedural and offline: no CDN, font, image, analytics, or external API is required.
- The records are preserved as supplied and retain `UNVERIFIED` labels where the brief did not establish a fact.
- No piracy site is visited, streamed from, downloaded from, or queried by the public map.

## Run locally

Open `map/index.html` directly in a browser, or run a static server from the project root:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000/map/index.html
```

## Data flow

`data/sites-private.csv` is the detailed working tier. `scripts/redact-public.py` generates `data/sites-public.csv` from it by keeping only `name,status,category`. The map has a generated embedded copy of the public rows so it works from `file://` without CORS issues.

## Included counts

- Public records: 342 rows
- Statuses: UP 142 · DEAD 91 · UNKNOWN 66 · MIRROR 22 · SEIZED 21
- Enforcement tables: arrests, seizures, and takedowns from the supplied compilation

This is an archival/research interface, not an operational directory.

## Static deployment

The repository is ready for GitHub Pages and Cloudflare Pages. Deploy the project root as the publish directory. `index.html`, `.nojekyll`, `_headers`, `_redirects`, and all links use local relative paths. No Manus URL or hosted runtime is required. The symbol favicon is at `assets/favicon.svg`; every HTML page references it.

The promo kit includes local SVG banners, an animated SVG, generated PNG illustrations, and looping GIFs under `assets/promo/`.
