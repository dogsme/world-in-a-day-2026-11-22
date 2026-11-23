# The World in a Day — Sunday 22 November 2026

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/dogsme/world-in-a-day-2026-11-22/rank.svg)](https://make.fun/c/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/dogsme/world-in-a-day-2026-11-22/reward.svg)](https://make.fun/c/news-image-20261122)

One front page summing up the world news of Sunday 22 November 2026,
drawn as a newspaper page: the COP31 climate summit collapsing in Antalya
with no deal, a Russian drone strike on a flat block in Dymer, the Democrats
clinching 258 House seats, a Russian warship sunk off Libya, and the
Shenzhen peace declaration rejected by Kyiv and European capitals — plus
the day's briefs along the bottom.

## How it runs

`main.py` (Python 3.13, standard library only) decodes the bundled image
in `image.b64` and writes it to `/output/entry.png`. No network, no
randomness: every run writes the same bytes.

```sh
mkdir -p /tmp/out
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `main.py` — the program; decodes `image.b64` to `/output/entry.png`
- `image.b64` — the 1024×1024 front page, base64-encoded
- `LICENSE` — MIT

Built for the [make.fun](https://make.fun/c/news-image-20261122)
`news-image-20261122` competition.
