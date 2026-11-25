#!/usr/bin/env python3
"""Render the 25 November 2026 world-news front page (1024x1024 PNG).

Build-time script only: it draws news.png from the headlines researched on
25 Nov 2026 (Reuters world-news summary, BBC, AP, Washington Post). The
graded entry is main.py, which only copies the finished news.png to
/output/entry.png -- no network, no randomness, byte-identical every run.
"""
import math

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
RED = (163, 22, 33)
GREY = (90, 86, 78)
RULE = (180, 172, 156)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_para(draw, x, y, text, fnt, max_w, leading, color=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 36  # margin

# ---- top kicker ----
d.rectangle([M, 22, W - M, 24], fill=INK)
d.text((M, 32), "WEDNESDAY, 25 NOVEMBER 2026", font=font(SANS_B, 21), fill=INK)
d.text((W - M - d.textlength("THE WORLD IN ONE PAGE", font(SANS_B, 21)), 32),
       "THE WORLD IN ONE PAGE", font=font(SANS_B, 21), fill=RED)

# ---- masthead ----
d.text((M, 56), "THE WORLD", font=font(SERIF_B, 96), fill=INK)
d.text((W - M - d.textlength("IN ONE IMAGE", font(SERIF_B, 36)), 96),
       "IN ONE IMAGE", font=font(SERIF_B, 36), fill=RED)
d.rectangle([M, 182, W - M, 186], fill=INK)
d.text((M, 192), "One day. One image. All the news that mattered.",
       font=font(SERIF_I, 24), fill=GREY)

# ---- lead story ----
LY = 232
d.rectangle([M, LY, W - M, LY + 4], fill=RED)
d.text((M, LY + 12), "LEAD STORY  •  WAR IN EUROPE", font=font(SANS_B, 19), fill=RED)

headline = "Ukraine confirms drone strike on Russian ship"
y = draw_para(d, M, LY + 40, headline, font(SERIF_B, 46), 600, 52)
deck = ("President Zelenskiy says Kyiv was behind Saturday's drone attack "
        "on a Russian cargo ship in the Gulf of Finland. Norway urges "
        "caution; Putin warns retaliation is \u2018inevitable\u2019.")
y = draw_para(d, M, y + 6, deck, font(SERIF, 21), 600, 27)
d.text((M, y + 8), "Kyiv claims the strike; Moscow vows a response.",
       font=font(SERIF_I, 21), fill=GREY)
lead_bottom = y + 40

# illustration: sea, ship, drones, burst (right of lead text)
ix0, iy0, ix1, iy1 = 668, LY + 40, W - M, LY + 40 + 196
d.rectangle([ix0, iy0, ix1, iy1], outline=INK, width=2)
d.rectangle([ix0, iy0, ix1, iy0 + 100], fill=(198, 222, 235))  # sky
d.rectangle([ix0, iy0 + 100, ix1, iy1], fill=(38, 84, 124))   # sea
d.ellipse([ix0 + 16, iy0 + 14, ix0 + 58, iy0 + 56], fill=(250, 214, 120))  # sun
# ship hull + containers
d.polygon([(ix0 + 26, iy0 + 110), (ix0 + 292, iy0 + 110),
           (ix0 + 266, iy0 + 146), (ix0 + 52, iy0 + 146)], fill=(30, 30, 34))
d.rectangle([ix0 + 62, iy0 + 82, ix0 + 108, iy0 + 110], fill=(163, 22, 33))
d.rectangle([ix0 + 114, iy0 + 82, ix0 + 160, iy0 + 110], fill=(210, 180, 60))
d.rectangle([ix0 + 166, iy0 + 82, ix0 + 212, iy0 + 110], fill=(90, 110, 90))
d.rectangle([ix0 + 218, iy0 + 92, ix0 + 238, iy0 + 110], fill=(220, 220, 210))
# explosion burst above the ship
cx, cy = ix0 + 252, iy0 + 52
for ang, ln in [(0, 30), (45, 23), (90, 30), (135, 23), (180, 30),
                (225, 23), (270, 30), (315, 23)]:
    x2 = cx + ln * math.cos(math.radians(ang))
    y2 = cy + ln * math.sin(math.radians(ang))
    d.line([(cx, cy), (x2, y2)], fill=(230, 120, 30), width=5)
d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=(240, 90, 20))
# two drones
for dx, dy in [(ix0 + 90, iy0 + 26), (ix0 + 150, iy0 + 16)]:
    d.ellipse([dx - 4, dy - 4, dx + 4, dy + 4], fill=INK)
    d.line([(dx - 12, dy - 8), (dx + 12, dy - 8)], fill=INK, width=2)
    d.line([(dx - 12, dy + 8), (dx + 12, dy + 8)], fill=INK, width=2)
d.text((ix0 + 8, iy1 - 26), "GULF OF FINLAND", font=font(SANS_B, 15), fill=(255, 255, 255))

# ---- story grid: 3 columns x 2 rows ----
GY = lead_bottom + 22
d.rectangle([M, GY - 12, W - M, GY - 10], fill=RULE)
stories = [
    ("MIDDLE EAST", "Houthi drone hits Riyadh's tallest tower",
     "Eleven wounded in the strike on the Saudi capital; the Saudi-led "
     "coalition condemns a \u201cterrorist attack\u201d."),
    ("WASHINGTON", "Trump awards Giuliani the Medal of Freedom",
     "The former New York mayor is honoured at the White House on "
     "Thanksgiving eve, as two turkeys are pardoned."),
    ("TECH", "Huawei guilty of stealing trade secrets",
     "A US jury convicts the Chinese giant of trade-secret theft — "
     "but clears it of racketeering."),
    ("EUROPE", "NATO to send early-warning jets to Poland",
     "The move follows missiles landing in Poland during an attack "
     "on Ukraine, allies say."),
    ("WASHINGTON", "CIA and spy chief's office hit by cyber breach",
     "Unclassified information is taken in a breach of America's top "
     "intelligence agencies, sources say."),
    ("THE GULF", "Three oil tankers \u2018hit by mines\u2019 in Hormuz",
     "Iran's Revolutionary Guard Navy says naval mines struck the "
     "tankers in the vital oil strait."),
]
col_w = (W - 2 * M - 2 * 20) // 3
row_h = 178
for i, (tag, head, body) in enumerate(stories):
    cx0 = M + (i % 3) * (col_w + 20)
    cy0 = GY + (i // 3) * row_h
    d.text((cx0, cy0), f"{i + 2}.  {tag}", font=font(SANS_B, 16), fill=RED)
    y = draw_para(d, cx0, cy0 + 23, head, font(SERIF_B, 25), col_w, 29)
    draw_para(d, cx0, y + 3, body, font(SERIF, 19), col_w, 24, color=(50, 48, 44))

# ---- also today strip ----
AY = GY + 2 * row_h + 8
d.rectangle([M, AY, W - M, AY + 2], fill=INK)
d.text((M, AY + 10), "ALSO TODAY", font=font(SANS_B, 18), fill=RED)
also = ("Sarkozy corruption case sent to trial  •  5.6 quake shakes Nepal  •  "
        "England beat Australia in the 2nd T20I  •  International Day for the "
        "Elimination of Violence against Women")
draw_para(d, M, AY + 36, also, font(SERIF, 20), W - 2 * M, 26)

# ---- footer ----
FY = H - 46
d.rectangle([M, FY - 12, W - M, FY - 10], fill=RULE)
d.text((M, FY), "Sources: Reuters · BBC · AP · The Washington Post — as reported 25 November 2026",
       font=font(SANS, 16), fill=GREY)
d.text((W - M - d.textlength("make.fun/news-image-20261125", font(SANS, 16)), FY),
       "make.fun/news-image-20261125", font=font(SANS, 16), fill=GREY)

img.save("/home/hatch/workspace/makefun/news-image-20261125-entry/news.png", optimize=True)
print("saved news.png")
