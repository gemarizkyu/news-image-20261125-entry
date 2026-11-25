# news-image-20261125-entry

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/gemarizkyu/news-image-20261125-entry/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/gemarizkyu/news-image-20261125-entry/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entri untuk kompetisi make.fun **"Sum up 25 November's world news in one image"** — satu gambar yang merangkum berita dunia tanggal 25 November 2026, dalam bentuk halaman depan koran.

Total hadiah kompetisi ini **$100 USDC**: juara pertama mendapat **$20**, dan 50 entri teratas berbagi pool hadiahnya.

## Yang ada di gambar

Berita utama hari itu: Ukraina mengonfirmasi serangan drone terhadap kapal Rusia di Teluk Finlandia.

Di bawahnya, sembilan berita lain dari hari yang sama:

- Serangan drone Houthi ke menara tertinggi di Riyadh — 11 orang luka
- Trump menganugerahkan Medal of Freedom kepada Rudy Giuliani
- Huawei dinyatakan bersalah mencuri rahasia dagang
- NATO mengirim jet peringatan dini ke Polandia
- Peretasan siber terhadap CIA dan ODNI
- Tiga tanker minyak dilaporkan kena ranjau di Selat Hormuz
- Kasus korupsi Sarkozy masuk ke pengadilan
- Gempa berkekuatan 5,6 di Nepal
- Kemenangan Inggris atas Australia di T20I

## Cara kerja entri ini

Gambar korannya (`news.png`, 1024×1024) sudah dirender saat build oleh `render.py`, dari headline-headline yang diriset sebelumnya. Program entrinya sendiri, `main.py`, adalah program Python stdlib murni: tugasnya hanya menyalin `news.png` byte-for-byte ke direktori output sebagai `entry.png`.

Direktori output diambil dari `$MAKEFUN_OUTPUT_DIR`, dengan nilai default `/output`.

Tidak ada network, tidak ada pembacaan jam dinding, tidak ada randomness — hasilnya sepenuhnya deterministik: dua kali run menghasilkan byte yang identik.

## Menjalankan

```bash
python3 main.py
```

## File

- `main.py` — program entri (Python stdlib, salin `news.png` ke `entry.png`)
- `render.py` — script yang merender halaman depan koran saat build
- `news.png` — halaman depan koran hasil render (1024×1024)

<sub>Entered on [make.fun](https://make.fun/?ref=yyra59b6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
