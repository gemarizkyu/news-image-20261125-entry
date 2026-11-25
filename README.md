# news-image-20261125-entry

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/gemarizkyu/news-image-20261125-entry/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/gemarizkyu/news-image-20261125-entry/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Sum up the world's news of Wednesday 25 November 2026 in one image. The entry is a program that writes one image to `/output/entry.png`: a newspaper front page — "THE WORLD in one image" — drawn from the real headlines of the day, researched from Reuters, BBC, AP and the Washington Post.

Lead story: Ukraine confirms a drone strike on a Russian ship in the Gulf of Finland. Also in the image: the Houthi drone hit on Riyadh's tallest tower (11 wounded), Trump awarding Rudy Giuliani the Medal of Freedom, Huawei found guilty of stealing trade secrets, NATO sending early-warning jets to Poland, the CIA and ODNI cyber breach, and three oil tankers reportedly hit by mines in the Strait of Hormuz — plus Sarkozy's corruption case going to trial, a 5.6 quake in Nepal, and England's T20I win over Australia.

## Run it

```sh
python3 main.py
# writes entry.png (1024x1024, PNG) to $MAKEFUN_OUTPUT_DIR (default /output)
```

`main.py` is pure Python stdlib: it copies the finished front page (`news.png`, rendered at build time by `render.py` from the researched headlines) byte-for-byte to the output directory. No network, no wall clock, no randomness — two runs write identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=gru-gaming&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
