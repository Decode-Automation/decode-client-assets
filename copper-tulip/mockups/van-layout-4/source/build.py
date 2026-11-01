"""Copper Tulip homepage — van theme, Set A / Layout 4.

Editable source for the mockup Kily picked on 1 Nov 2026. Rebuilt from the
original Set A / Layout 4 renders (../original/) because no editable source
existed. Every later round edits THIS file, then re-renders.

    python3 build.py            # writes ../round-N/index.html and the PNG renders
    python3 build.py --round 2  # choose the output round folder

Needs: playwright (chromium). Fonts: Arimo (metric-identical to Liberation Sans,
which is what renders when Arimo isn't installed). Photos come from
../../../photos/ (Kily's real photos, resized for web).
"""
import argparse, asyncio, os, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent  # mockups/van-layout-4
PHOTOS = "../../../photos"   # relative to a round folder
LOGO = "../../../brand/lockup-cream-no-gift-wrapping.png"

def ph(n):
    return f"{PHOTOS}/20267-31TheCopperTulip{n}.jpg"

# ---------------------------------------------------------------- content
# Kily's words (1 Nov email) are kept as written. Nothing invented: no phone,
# no town, no reviews. Facts from the 23 Oct kickoff answers are marked (K).
C = {
    "banner": "Follow the flowers- find us on social media @thecoppertulip",
    "nav": ["Packages", "How it works", "Extras", "FAQ"],
    "cta": "Find your event date",
    "hero_eyebrow": "The interactive party favor",
    "hero_h1": "Fresh Flowers",
    "hero_h2": "Build Your Own Bouquet",
    "hero_body": ("We set up our cart and create a space for your guests to pick their own "
                  "flowers and create their own bouquet. An interactive party favor for corporate "
                  "events, employee appreciation and brand launches."),
    "occasions": ["Corporate events", "Employee appreciation", "Brand launches", "Showers & birthdays"],
    "meet_eyebrow": "Meet the flower bar",
    "meet_h": "A party activity, a centerpiece and a favor in one.",
    "meet_body": ("Our cart, loaded with fresh stems in your colors. Every guest builds a bouquet "
                  "and takes it home as their favor."),
    "steps": [
        ("Find your event date", "Pick your date and tell us a little about your event."),
        ("We reach out", "We will reach out to you to talk color, inspiration & flower requests."),
        ("Create something they love", "We set up our flower cart and help your guests create something they love."),
    ],
    "feat_eyebrow": "Every guest goes home happy",
    "feat_h": "Small bouquet. Big moment.",
    "feat_body": ("Waterproof bouquet wraps to complement your event and ribbon are included, "
                  "so every guest leaves with a finished bouquet."),
    "pk_eyebrow": "Packages",
    "pk_h": "Choose your flower bar.",
    "packages": [
        {"name": "Classic", "price": "$40", "photo": 55, "pos": "50% 60%",
         "desc": ("Our cart loaded with the perfect colorway for your event. This package is perfect "
                  "for any flower lover and gives guests the perfect party favor to enjoy in their home."),
         "rows": ["7–9 stems per bouquet", "Roses, seasonal flowers, fillers and greenery",
                  "Wraps and ribbon included"],
         "note": None},
        {"name": "Designer", "price": "$65", "photo": 73, "pos": "40% 50%",
         "desc": ("A whimsical collection that brings in delicate blooms & fun textures that you don’t "
                  "see every day, with extra premium stems that create a designer feel, bringing "
                  "movement and whimsy into every bouquet."),
         "rows": ["12–14 stems per bouquet", "Roses, seasonal flowers and fillers, plus premium stems",
                  "Wraps and ribbon included"],
         "note": ("Some of our favorites in this package include anemones, ranunculus, imported fancy "
                  "tulips, freesia and even dyed specialty flowers that create a whole vibe!")},
    ],
    "pk_both": ("Both packages include bar setup, clean up, and all supplies needed to make a bouquet. "
                "Waterproof bouquet wraps and ribbon are included; pre-ribboned flower holders are an upgrade."),
    # (K) minimum, extra hour, over-30 quote. $150 setup line left off: see Clarifications #16.
    "pk_fine": "$600 event minimum · $75 per extra hour past two hours · More than 30 guests? We’ll quote it.",
    "seasonal_eyebrow": "Seasonal bouquets",
    "seasonal_h": "Seasonal bouquets, ready to pre-order.",
    "seasonal_body": "Holiday bouquets and seasonal specials, ordered ahead. Pick yours, pay online, and pick it up.",
    "seasonal_btn": "See seasonal bouquets",
    "story_eyebrow": "All supplies included",
    "story_h": "We bring the whole flower bar.",
    "story_body": ("Bar setup, clean up, shears, wraps, ribbon and every stem. Our floral assistants run "
                   "the cart while your guests build their bouquets."),
    "ex_eyebrow": "Extras",
    "ex_h": "Need extra decor or something special?",
    "extras": [("Vase add-on", "$5 each"), ("Ribboned flower carrier", "$4 each"),
               ("Flower crown", "$45"), ("Bud vase", "$35"),
               ("Small arrangement", "$65"), ("Large arrangement", "$120")],
    "ex_photos": [(13, "50% 45%", "Ribboned flower carriers"), (83, "50% 55%", "Arrangements"),
                  (37, "50% 40%", "Bud vases")],
    "faq": [
        ("What happens after I find my date?",
         "We reach out to talk color, inspiration and flower requests, then send a 50% deposit invoice. Pay within 7 days to hold your date."),
        ("How far ahead should I book?", "At least a week before your event."),
        ("Is there a minimum?", "Yes. Our event minimum is $600."),
        ("Can the party run longer than two hours?", "Yes. Extra time is $75 an hour."),
        ("We have more than 30 guests. Can you do it?", "Yes. We’ll put together a custom quote."),
        ("Can I add vases or flower carriers?", "Yes. Vases are $5 each and ribboned flower carriers are $4 each."),
    ],
    "end_kicker": "Let’s bloom",
    "end_h": "Have a date in mind?",
    "end_body": "Find your event date and we’ll reach out to talk color, inspiration and flower requests.",
    "footer_note": ("Mockup for review. Photos are The Copper Tulip’s own. Logo is an interim lockup until "
                    "the van logo file arrives. Fonts are stand-ins until the brand fonts are licensed for web."),
}

# Review notes drawn on the frame (yellow tags). Remove for the build.
NOTES = {
    "logo": "Interim logo: closest lockup we have (cream). Swap for the light van logo file when Kily sends it.",
    "seasonal": "Planned: Kily edits this section from her app.",
}

# ---------------------------------------------------------------- page
CSS = r"""
:root{--peach:#F4A981;--cream:#FCF7EE;--blush:#FAEEE4;--green:#4C7E5C;--green-d:#3E6B4F;--teal:#2E5E61;
--copper:#C8613A;--ink:#2a2f2c;--body:#5d625f;--rule:#e6dccd;--w:1120px}
*{box-sizing:border-box}html,body{margin:0}
body{background:var(--cream);color:var(--body);font-family:Arimo,"Liberation Sans",Arial,sans-serif;font-size:17px;line-height:1.55}
h1,h2,h3{color:var(--green-d);margin:0;letter-spacing:-.01em;line-height:1.12}
.wrap{width:var(--w);max-width:calc(100% - 40px);margin:0 auto}
.eyebrow{font-size:12.5px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--copper);margin:0 0 14px}
.btn{display:inline-block;background:var(--green);color:#fff;font-weight:700;font-size:16px;padding:14px 28px;border-radius:999px;text-decoration:none;border:2px solid var(--green)}
.btn.ghost{background:transparent;color:var(--green)}
/* scallops */
.sc-down{height:40px;background-image:radial-gradient(circle 60px at 50% -20px,var(--c) 59.5px,transparent 60px);background-repeat:repeat-x;background-size:118px 40px;background-position:-2px 0}
.sc-up{height:40px;background-image:radial-gradient(circle 60px at 50% calc(100% + 20px),var(--c) 59.5px,transparent 60px);background-repeat:repeat-x;background-size:118px 40px;background-position:-2px 0}
/* banner */
.banner{background:var(--peach);text-align:center;color:var(--ink);font-size:13.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;padding:14px 20px 4px}
.banner b{letter-spacing:.06em;text-transform:none;font-size:15px}
.banner+.sc-down{--c:var(--peach)}
/* header */
header{position:relative}
.hdr{display:flex;align-items:center;justify-content:space-between;height:150px}
.logo{display:block;width:132px;height:132px;margin-top:-26px}
.logo img{width:100%;height:100%;object-fit:contain;display:block}
nav{display:flex;gap:34px;font-size:16.5px;color:var(--ink);margin-left:-60px}
/* hero */
.hero{position:relative;height:760px;background:#ddd center/cover no-repeat}
.hero .ph,.story .ph{display:none}
.hero .card{position:absolute;left:calc(50% - var(--w)/2);top:130px;width:590px;background:var(--cream);border-radius:24px;padding:44px 44px 40px}
.hero h1{font-size:70px;white-space:nowrap;line-height:1;font-weight:700;color:var(--green-d);letter-spacing:-.025em}
.hero h2{font-size:31px;font-weight:400;color:var(--teal);margin:12px 0 20px}
.hero p{margin:0 0 30px;font-size:17.5px}
.hero .btns{display:flex;gap:14px;flex-wrap:wrap}
.occ{background:var(--green);color:#fff;text-align:center;font-size:13.5px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;padding:30px 20px 12px}
.occ span{margin:0 22px;white-space:nowrap}
.occ+.sc-down{--c:var(--green)}
/* meet */
.meet{padding:96px 0 40px}
.meet .top{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:end}
.meet h2{font-size:46px;line-height:1.08}
.meet .top p{font-size:19px;margin:0 0 8px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:64px}
.step{border-top:1.5px solid var(--rule);padding-top:20px}
.step .n{color:var(--copper);font-size:20px}
.step h3{font-size:22px;margin:2px 0 8px}
.step p{margin:0;font-size:16px}
.feat{display:grid;grid-template-columns:528px 1fr;gap:64px;align-items:center;padding:56px 0 100px}
.feat .img{height:440px;border-radius:22px;background:center/cover no-repeat}
.feat h2{font-size:46px;line-height:1.08;margin-bottom:18px}
.feat p{font-size:19px;margin:0}
/* packages */
.pk-top{--c:var(--green);background-color:var(--cream)}
.pk{background:var(--green);padding:56px 0 64px;color:#e8efe9}
.pk .eyebrow{color:var(--peach)}
.pk h2{color:#fff;font-size:46px;margin-bottom:40px}
.pcards{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.pc{color:var(--body);background:#fff;border-radius:22px;overflow:hidden;display:flex;flex-direction:column}
.pc .img{height:330px;background:center/cover no-repeat}
.pc .b{padding:28px 30px 30px;display:flex;flex-direction:column;flex:1}
.pc h3{font-size:24px}
.pc .price{color:var(--green-d);font-size:38px;font-weight:700;margin:6px 0 12px}
.pc .price small{font-size:16px;font-weight:400;color:var(--body)}
.pc .desc{margin:0 0 14px;font-size:16px}
.pc ul{list-style:none;padding:0;margin:0 0 6px}
.pc li{border-top:1px solid #efe7da;padding:10px 0;font-size:15.5px}
.pc .fav{font-size:14.5px;color:var(--copper);margin:6px 0 0}
.pc .sp{flex:1;min-height:20px}
.pc .btn{text-align:center}
.pk .both{font-size:17px;color:#fff;margin:34px 0 8px;max-width:860px}
.pk .fine{font-size:15px;margin:0}
.pk-bot{--c:var(--green);background-color:var(--cream)}
/* seasonal */
.seas{display:grid;grid-template-columns:1fr 528px;gap:64px;align-items:center;padding:90px 0 100px}
.seas h2{font-size:46px;line-height:1.08;margin-bottom:18px}
.seas p{font-size:19px;margin:0 0 28px}
.seas .img{height:560px;border-radius:22px;background:center/cover no-repeat}
/* story */
.story{position:relative;height:600px;background:center/cover no-repeat}
.story .card{position:absolute;left:calc(50% - var(--w)/2);top:130px;width:470px;background:var(--cream);border-radius:22px;padding:40px}
.story h2{font-size:42px;line-height:1.1;margin-bottom:16px}
.story p{margin:0;font-size:17px}
/* extras */
.ex{background:var(--teal);color:#dfe9e8;padding:90px 0 100px}
.ex .eyebrow{color:var(--peach)}
.ex h2{color:#fff;font-size:46px;margin-bottom:40px}
.exph{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:48px}
.exph div{height:300px;border-radius:20px;background:center/cover no-repeat}
.exl{display:grid;grid-template-columns:repeat(3,1fr);column-gap:24px;row-gap:28px}
.exl div{border-top:1px solid rgba(255,255,255,.28);padding-top:16px}
.exl h3{color:#fff;font-size:21px;font-weight:700;margin-bottom:2px}
.exl p{margin:0;font-size:17px}
/* faq */
.faq{padding:96px 0 100px;text-align:center}
.faq h2{font-size:46px;margin-bottom:28px}
.faq .list{width:796px;max-width:100%;margin:0 auto;text-align:left;display:grid;gap:12px}
.faq .q{background:#fff;border-radius:16px;padding:20px 22px}
.faq .q h3{font-size:17.5px;margin-bottom:6px}
.faq .q p{margin:0;font-size:16px}
/* end */
.end{background:var(--blush);text-align:center;padding:90px 20px 94px}
.end .k{font-size:30px;color:var(--teal);margin:0}
.end h2{font-size:48px;margin:0 0 20px}
.end p{font-size:19px;max-width:560px;margin:0 auto 32px}
.ft-top{--c:var(--peach);background-color:var(--blush)}
footer{background:var(--peach);color:var(--ink);padding:44px 0 56px}
footer .row{display:flex;gap:56px;align-items:center}
footer img{width:96px;height:96px;object-fit:contain}
footer h4{margin:0 0 6px;font-size:13.5px;letter-spacing:.16em;text-transform:uppercase}
footer p{margin:0;font-size:16px}
.mk{background:#263a2f;color:#d9e2dc;font-size:13px;padding:10px 40px}
/* review notes */
.note{position:absolute;z-index:5;background:#FFE45C;color:#222;font:600 13px/1.35 Arimo,"Liberation Sans",sans-serif;padding:9px 12px;border-radius:6px;box-shadow:0 2px 0 rgba(0,0,0,.15);max-width:270px}
.note:before{content:"REVIEW NOTE ";font-weight:800;letter-spacing:.06em}
header .note{left:calc(50% - var(--w)/2 + 150px);top:92px}
.seas{position:relative}.seas .note{left:0;top:40px}

@media (max-width:760px){
 :root{--w:100%}
 body{font-size:16px}
 .wrap{max-width:calc(100% - 36px)}
 .banner{font-size:11px;letter-spacing:.1em;padding:12px 14px 2px}
 .banner b{font-size:12.5px}
 .sc-down,.sc-up{height:24px;background-size:64px 24px;background-image:radial-gradient(circle 33px at 50% -10px,var(--c) 32.5px,transparent 33px)}
 .sc-up{background-image:radial-gradient(circle 33px at 50% calc(100% + 10px),var(--c) 32.5px,transparent 33px)}
 .hdr{height:118px}
 .logo{width:104px;height:104px;margin-top:-16px}
 nav{display:none}
 .hdr .btn{font-size:14.5px;padding:11px 18px}
 .hero{height:auto;background:none!important}
 .hero .ph,.story .ph{display:block}
 .hero .ph{height:340px;background:center/cover no-repeat}
 .hero .card{position:relative;left:auto;top:auto;width:auto;margin:-70px 14px 0;padding:30px 22px 28px}
 .hero h1{font-size:52px}
 .hero h2{font-size:23px}
 .hero p{font-size:16.5px}
 .occ{font-size:11.5px;letter-spacing:.18em;padding:26px 16px 10px;line-height:2.1}
 .occ span{display:block;margin:0}
 .hero-wrap{padding-bottom:34px}
 .meet{padding:56px 0 20px}
 .meet .top{grid-template-columns:1fr;gap:18px}
 .meet h2,.feat h2,.pk h2,.seas h2,.ex h2,.faq h2{font-size:32px}
 .meet .top p,.feat p,.seas p{font-size:17px}
 .steps{grid-template-columns:1fr;gap:26px;margin-top:36px}
 .feat{grid-template-columns:1fr;gap:28px;padding:40px 0 64px}
 .feat .img{height:290px}
 .pk{padding:40px 0 48px}
 .pk h2{margin-bottom:26px}
 .pcards{grid-template-columns:1fr;gap:20px}
 .pc .img{height:240px}
 .pc .b{padding:24px 22px 24px}
 .seas{grid-template-columns:1fr;gap:28px;padding:56px 0 64px}
 .seas .img{height:380px;order:2}
 .seas .note{position:relative;top:auto;margin-bottom:10px}
 .story{height:auto;background:none!important}
 .story .ph{height:280px;background:center/cover no-repeat}
 .story .card{position:relative;left:auto;top:auto;width:auto;margin:-60px 14px 0;padding:28px 22px}
 .story h2{font-size:30px}
 .story-wrap{padding-bottom:48px}
 .ex{padding:56px 0 64px}
 .ex h2{margin-bottom:26px}
 .exph{grid-template-columns:1fr 1fr;gap:12px;margin-bottom:32px}
 .exph div{height:190px}
 .exph div:first-child{grid-column:1/3;height:240px}
 .exl{grid-template-columns:1fr 1fr;row-gap:22px;column-gap:16px}
 .exl h3{font-size:18px}
 .faq{padding:56px 0 64px}
 .end{padding:60px 20px 64px}
 .end .k{font-size:24px}.end h2{font-size:34px}.end p{font-size:17px}
 footer .row{flex-direction:column;align-items:flex-start;gap:22px}
 .mk{padding:10px 18px}
 header .note{left:128px;top:76px;max-width:220px;font-size:11.5px}
}
"""

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def bg(n, pos="50% 50%"):
    return f"background-image:url('{ph(n)}');background-position:{pos}"

def page(notes=True):
    c = C
    o = []
    a = o.append
    a("<!doctype html><html lang=en><head><meta charset=utf-8>"
      "<meta name=viewport content='width=device-width,initial-scale=1'>"
      f"<title>The Copper Tulip — Pop-up flower bar</title><style>{CSS}</style></head><body>")
    banner = esc(c["banner"]).replace("@thecoppertulip", "<b>@thecoppertulip</b>")
    a(f"<div class=banner>{banner}</div><div class=sc-down></div>")
    a("<header><div class='wrap hdr'>"
      f"<a class=logo href='#'><img src='{LOGO}' alt='The Copper Tulip, pop-up flower bar'></a>"
      "<nav>" + "".join(f"<span>{esc(x)}</span>" for x in c["nav"]) + "</nav>"
      f"<a class=btn href='#'>{esc(c['cta'])}</a></div>")
    if notes: a(f"<div class=note>{esc(NOTES['logo'])}</div>")
    a("</header>")
    # hero: photo 49 (no cart sign). 94 not used: its badge reads "gift wrapping".
    a(f"<div class=hero-wrap><section class=hero style=\"{bg(49,'50% 62%')}\"><div class=ph style=\"{bg(49,'55% 60%')}\"></div>"
      f"<div class=card><p class=eyebrow>{esc(c['hero_eyebrow'])}</p><h1>{esc(c['hero_h1'])}</h1>"
      f"<h2>{esc(c['hero_h2'])}</h2><p>{esc(c['hero_body'])}</p><div class=btns>"
      f"<a class=btn href='#'>{esc(c['cta'])}</a><a class='btn ghost' href='#'>See packages</a></div></div></section></div>")
    a("<div class=occ>" + "".join(f"<span>{esc(x)}</span>" for x in c["occasions"]) + "</div><div class=sc-down></div>")
    # meet + steps
    a(f"<section class='wrap meet'><div class=top><div><p class=eyebrow>{esc(c['meet_eyebrow'])}</p>"
      f"<h2>{esc(c['meet_h'])}</h2></div><p>{esc(c['meet_body'])}</p></div><div class=steps>")
    for i, (t, d) in enumerate(c["steps"], 1):
        a(f"<div class=step><div class=n>Step {i}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>")
    a("</div></section>")
    a(f"<section class='wrap feat'><div class=img style=\"{bg(62,'50% 42%')}\"></div><div>"
      f"<p class=eyebrow>{esc(c['feat_eyebrow'])}</p><h2>{esc(c['feat_h'])}</h2><p>{esc(c['feat_body'])}</p></div></section>")
    # packages
    a("<div class='sc-up pk-top'></div><section class=pk><div class=wrap>"
      f"<p class=eyebrow>{esc(c['pk_eyebrow'])}</p><h2>{esc(c['pk_h'])}</h2><div class=pcards>")
    for p in c["packages"]:
        a(f"<div class=pc><div class=img style=\"{bg(p['photo'],p['pos'])}\"></div><div class=b>"
          f"<h3>{esc(p['name'])}</h3><div class=price>{p['price']} <small>per guest</small></div>"
          f"<p class=desc>{esc(p['desc'])}</p><ul>" + "".join(f"<li>{esc(r)}</li>" for r in p["rows"]) + "</ul>")
        if p["note"]: a(f"<p class=fav>{esc(p['note'])}</p>")
        a(f"<div class=sp></div><a class=btn href='#'>Check this date</a></div></div>")
    a(f"</div><p class=both>{esc(c['pk_both'])}</p><p class=fine>{esc(c['pk_fine'])}</p></div></section>"
      "<div class='sc-down pk-bot'></div>".replace("sc-down pk-bot", "sc-down pk-bot") )
    # seasonal
    a(f"<section class='wrap seas'>")
    if notes: a(f"<div class=note>{esc(NOTES['seasonal'])}</div>")
    a(f"<div><p class=eyebrow>{esc(c['seasonal_eyebrow'])}</p><h2>{esc(c['seasonal_h'])}</h2>"
      f"<p>{esc(c['seasonal_body'])}</p><a class=btn href='#'>{esc(c['seasonal_btn'])}</a></div>"
      f"<div class=img style=\"{bg(77,'50% 45%')}\"></div></section>")
    # story / supplies
    a(f"<div class=story-wrap><section class=story style=\"{bg(52,'50% 55%')}\"><div class=ph style=\"{bg(52,'45% 55%')}\"></div>"
      f"<div class=card><p class=eyebrow>{esc(c['story_eyebrow'])}</p><h2>{esc(c['story_h'])}</h2>"
      f"<p>{esc(c['story_body'])}</p></div></section></div>")
    # extras
    a(f"<section class=ex><div class=wrap><p class=eyebrow>{esc(c['ex_eyebrow'])}</p><h2>{esc(c['ex_h'])}</h2><div class=exph>")
    for n, pos, alt in c["ex_photos"]:
        a(f"<div role=img aria-label='{esc(alt)}' style=\"{bg(n,pos)}\"></div>")
    a("</div><div class=exl>" + "".join(f"<div><h3>{esc(n)}</h3><p>{esc(pr)}</p></div>" for n, pr in c["extras"])
      + "</div></div></section>")
    # faq
    a("<section class='wrap faq'><p class=eyebrow>Good to know</p><h2>Flower bar FAQs</h2><div class=list>")
    for q, ans in c["faq"]:
        a(f"<div class=q><h3>{esc(q)}</h3><p>{esc(ans)}</p></div>")
    a("</div></section>")
    a(f"<section class=end><p class=k>{esc(c['end_kicker'])}</p><h2>{esc(c['end_h'])}</h2>"
      f"<p>{esc(c['end_body'])}</p><a class=btn href='#'>{esc(c['cta'])}</a></section>")
    a("<div class='sc-up ft-top'></div><footer><div class='wrap row'>"
      f"<img src='{LOGO}' alt=''>"
      "<div><h4>The Copper Tulip</h4><p>Pop-up flower bar</p></div>"
      "<div><h4>Follow</h4><p>@thecoppertulip · Instagram · Facebook</p></div>"
      "<div><h4>Book</h4><p>At least a week ahead</p></div></div></footer>")
    if notes: a(f"<div class=mk>{esc(c['footer_note'])}</div>")
    a("</body></html>")
    return "".join(o)

async def render(html_path, out_dir):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, w in (("desktop", 1440), ("mobile", 390)):
            pg = await b.new_page(viewport={"width": w, "height": 900}, device_scale_factor=2)
            await pg.goto(html_path.as_uri())
            await pg.wait_for_load_state("networkidle")
            await pg.screenshot(path=str(out_dir / f"{name}.png"), full_page=True)
            await pg.close()
        await b.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--round", default="1")
    ap.add_argument("--no-notes", action="store_true")
    args = ap.parse_args()
    out = ROOT / f"round-{args.round}"
    out.mkdir(exist_ok=True)
    f = out / "index.html"
    f.write_text(page(notes=not args.no_notes), encoding="utf-8")
    asyncio.run(render(f, out))
    print("wrote", f, "and renders")
