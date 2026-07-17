#!/usr/bin/env python3
"""Premium branded banner for the Omega Field Command repos.
1280x640 (GitHub social-preview + README hero). Rendered at 3x, LANCZOS down."""
import io
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = 3                      # supersample
W, H = 1280 * S, 640 * S
NAVY_TOP, NAVY_BOT = (10, 16, 32), (18, 27, 46)
CHROME = (238, 241, 246)
MUTE = (154, 167, 187)
BLUE = (30, 160, 255)
AMBER = (217, 164, 65)

FONT = "C:/Windows/Fonts/"
def f(name, px): return ImageFont.truetype(FONT + name, px * S)
wm   = f("seguisb.ttf", 62)     # wordmark
sub  = f("segoeui.ttf", 25)
cat  = f("seguisb.ttf", 15)
tag  = f("seguisb.ttf", 19)
byl  = f("segoeui.ttf", 16)

img = Image.new("RGB", (W, H), NAVY_TOP)
px = img.load()
# vertical gradient
for y in range(H):
    t = y / H
    px_row = tuple(int(NAVY_TOP[i] + (NAVY_BOT[i] - NAVY_TOP[i]) * t) for i in range(3))
    for x in range(W):
        px[x, y] = px_row

# faint hairline grid (tactical)
grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(grid)
step = 64 * S
for gx in range(0, W, step):
    gd.line([(gx, 0), (gx, H)], fill=(30, 160, 255, 10), width=1)
for gy in range(0, H, step):
    gd.line([(0, gy), (W, gy)], fill=(30, 160, 255, 10), width=1)
img = Image.alpha_composite(img.convert("RGBA"), grid)

# ambient electric-blue glow behind the emblem: layered, wider than tall,
# so it reads as diffuse light rather than a defined shape
cx, cy = W // 2, int(H * 0.30)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for rx, ry, a in ((int(W*0.30), int(H*0.22), 34),
                  (int(W*0.20), int(H*0.15), 40),
                  (int(W*0.11), int(H*0.10), 46)):
    gd.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(30, 160, 255, a))
glow = glow.filter(ImageFilter.GaussianBlur(70 * S // 3))
img = Image.alpha_composite(img, glow)

draw = ImageDraw.Draw(img)

def tracked_width(text, font, tracking):
    w = 0
    for ch in text:
        w += draw.textlength(ch, font=font) + tracking
    return w - tracking if text else 0

def draw_tracked(cx, y, text, font, fill, tracking):
    total = tracked_width(text, font, tracking)
    x = cx - total / 2
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking

# emblem mark
try:
    em = Image.open("C:/tmp/op-logos/omega-emblem.png").convert("RGBA")
    target = 150 * S
    ratio = target / em.height
    em = em.resize((int(em.width * ratio), target), Image.LANCZOS)
    img.paste(em, (cx - em.width // 2, int(H * 0.30) - em.height // 2), em)
except Exception as e:
    print("emblem skipped:", e)

CXf = W / 2
draw_tracked(CXf, int(H * 0.52), "OMEGA FIELD COMMAND", wm, CHROME, 8 * S)
# subtitle (not tracked, centered)
st = "Secure field operations and task force coordination for law enforcement"
draw.text((CXf, int(H * 0.66)), st, font=sub, fill=MUTE, anchor="mm")
# amber rule
rw = 130 * S
draw.rectangle([CXf - rw / 2, int(H * 0.735), CXf + rw / 2, int(H * 0.735) + 3 * S], fill=AMBER)
# category strip
draw_tracked(CXf, int(H * 0.775), "FRAUD DETECTION   CRITICAL INFRASTRUCTURE   PUBLIC SAFETY", cat, MUTE, 6 * S)
# tagline
draw_tracked(CXf, int(H * 0.86), "PROTECT.  ENABLE.  EMPOWER.", tag, BLUE, 10 * S)

out = img.convert("RGB").resize((1280, 640), Image.LANCZOS)
out.save("C:/Users/Hatchet/.claude/jobs/6eddec7e/tmp/ofc-banner.png", optimize=True)
print("banner written:", out.size)
