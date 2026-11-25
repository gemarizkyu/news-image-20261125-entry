#!/usr/bin/env python3
"""news-image-20261125 entry: sum up 25 November 2026's world news in one image.

The graded program writes one image to /output/entry.png. The image is a
newspaper front page ("THE WORLD in one image") drawn from the real headlines
of Wednesday 25 November 2026, researched from Reuters, BBC, AP and the
Washington Post: Ukraine confirms a drone strike on a Russian ship in the
Gulf of Finland (lead), the Houthi drone hit on Riyadh's tallest tower,
Trump awarding Giuliani the Medal of Freedom, Huawei's trade-secret
conviction, NATO early-warning jets for Poland, the CIA/ODNI cyber breach,
and oil tankers reportedly hit by mines in the Strait of Hormuz.

The finished page ships in this repository as news.png (1024x1024, under
1 MiB) and this program copies it byte-for-byte to the output directory:
no network, no wall clock, no randomness, so two runs write identical bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "news.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    size = target.stat().st_size
    print(f"wrote {target} ({size} bytes)")


if __name__ == "__main__":
    main()
