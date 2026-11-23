#!/usr/bin/env python3
"""The World in a Day - Sunday 22 November 2026.

Writes the day's front page to /output/entry.png. The image is bundled
with this program as base64 in image.b64; decoding it is the whole job,
so every run produces exactly the same bytes. Python 3.13 standard
library only, no network.
"""
import base64
import os
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    encoded = (here / "image.b64").read_text(encoding="ascii")
    png = base64.b64decode("".join(encoded.split()))
    if not png.startswith(b"\x89PNG"):
        raise ValueError("image.b64 does not decode to a PNG")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(png)
    print(f"wrote {target} ({len(png)} bytes)")


if __name__ == "__main__":
    main()
