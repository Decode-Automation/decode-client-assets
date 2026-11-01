"""Copper Tulip homepage — van theme, Set A / Layout 4.

Editable source for the layout Kily picked on 1 Nov 2026 (rebuilt from the
original renders in ../original/). Every round edits THIS file, then re-renders.

    python3 build.py --round 2            # writes ../round-2/index.html + renders
    python3 build.py --round 2 --no-notes # same page without the yellow review notes

One layout and one copy set (COPY["mockup"]). Add a second set to COPY to get a
picker bar for comparing wording (used in round 2).
Renders: desktop-<set>.png (1440 @2x) and mobile-<set>.png (390 @2x).

Needs: playwright (chromium). Fonts: Arimo (metric-identical to Liberation Sans).
Photos come from ../../../photos/ (Kily's real photos, resized for web).
"""
import argparse, asyncio, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent  # mockups/van-layout-4
PHOTOS = "../../../photos"   # relative to a round folder
LOGO = "../../../brand/lockup-cream-no-gift-wrapping.png"
BOOK = "https://portal.decodeautomation.com/book/copper-tulip"  # her live booking page

def ph(n):
    return f"{PHOTOS}/20267-31TheCopperTulip{n}.jpg"

# ---------------------------------------------------------------- shared facts
# Kily's words (1 Nov email) where marked. Nothing invented: no phone, no town,
# no reviews, no badge. Facts from the 23 Oct kickoff are marked (K).
CLASSIC_DESC = ("Our cart loaded with the perfect colorway for your event. This package is perfect "
                "for any flower lover and gives guests the perfect party favor to enjoy in their home.")
DESIGNER_DESC = ("A whimsical collection that brings in delicate blooms & fun textures that you don’t "
                 "see every day, with extra premium stems that create a designer feel, bringing "
                 "movement and whimsy into every bouquet.")
DESIGNER_FAV = ("Some of our favorites in this package include anemones, ranunculus, imported fancy "
                "tulips, freesia and even dyed specialty flowers that create a whole vibe!")

COPY = {}

# ---- Set 1: round 1 wording, Josh's 1 Nov notes applied -----------------------
# Changes from round 1: booking buttons say "Book your event" and open the booking
# page; See packages scrolls to packages; step 1 is a request linked to the booking
# page; step titles no longer repeat their descriptions; package buttons are
# "Book the Classic"/"Book the Designer"; the pricing-rules line under the packages
# is gone; footer Book column gone; the story section is back (Kily and Meg)
# in place of the supplies section.
COPY["mockup"] = {
    "label": "Mockup copy",
    "banner": "Follow the flowers- find us on social media @thecoppertulip",
    "cta": "Book your event",
    "hero_eyebrow": "Pop-up flower bar",
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
        ("Request your event", "Pick your date and tell us a little about your event.", True),
        ("We reach out", "We will reach out to you to talk color, inspiration & flower requests.", False),
        ("We bring the flower bar", "We set up our flower cart and help your guests create something they love.", False),
    ],
    "feat_eyebrow": "Every guest goes home happy",
    "feat_h": "Small bouquet. Big moment.",
    "feat_body": ("Waterproof bouquet wraps to complement your event and ribbon are included, "
                  "so every guest leaves with a finished bouquet."),
    "pk_eyebrow": "Packages",
    "pk_h": "Choose your flower bar.",
    "pk_intro": None,
    "packages": [
        {"name": "Classic", "price": "$40", "photo": 55, "pos": "50% 60%", "desc": CLASSIC_DESC,
         "rows": ["7–9 stems per bouquet", "Roses, seasonal flowers, fillers and greenery", "Wraps and ribbon included"],
         "note": None, "btn": "Book the Classic"},
        {"name": "Designer", "price": "$65", "photo": 73, "pos": "40% 50%", "desc": DESIGNER_DESC,
         "rows": ["12–14 stems per bouquet", "Roses, seasonal flowers and fillers, plus premium stems", "Wraps and ribbon included"],
         "note": DESIGNER_FAV, "btn": "Book the Designer"},
    ],
    "pk_both": ("Both packages include bar setup, clean up, and all supplies needed to make a bouquet. "
                "Waterproof bouquet wraps and ribbon are included; pre-ribboned flower holders are an upgrade."),
    "seasonal_eyebrow": "Seasonal bouquets",
    "seasonal_h": "Seasonal bouquets, ready to pre-order.",
    "seasonal_body": "Holiday bouquets and seasonal specials, ordered ahead. Pick yours, pay online, and pick it up.",
    "seasonal_btn": "See seasonal bouquets",
    "story_eyebrow": "Our story",
    "story_h": "Hi, we’re Kily and Meg.",
    "story_body": ("We spend a lot of time around weddings and events, and around here it was mostly basic "
                   "flower displays. Nobody was doing it like we wanted to, so we built a cart (and now "
                   "a van!), loaded it with single stems, and let your guests do the fun part."),
    "ex_eyebrow": "Extras",
    "ex_h": "Need extra decor or something special?",
    "extras": [("Vase add-on", "$5 each", None), ("Ribboned flower carrier", "$4 each", None),
               ("Flower crown", "$45", None), ("Bud vase", "$35", None),
               ("Small arrangement", "$65", None), ("Large arrangement", "$120", None)],
    "faq_eyebrow": "Good to know",
    "faq_h": "Flower bar FAQs",
    "faq": [
        ("What happens after I request a date?",
         "We reach out to talk color, inspiration and flower requests, then send a 50% deposit invoice. Pay within 7 days to hold your date."),
        ("How far ahead should I book?", "At least a week before your event."),
        ("Is there a minimum?", "Yes. Our event minimum is $600."),
        ("Can the party run longer than two hours?", "Yes. Extra time is $75 an hour."),
        ("We have more than 30 guests. Can you do it?", "Yes. We’ll put together a custom quote."),
        ("Can I add vases or flower carriers?", "Yes. Vases are $5 each and ribboned flower carriers are $4 each."),
    ],
    "contact_eyebrow": "Contact",
    "contact_h": "Questions?",
    "contact_body": ("Arrangements, a big group, or something we didn’t cover? Send us a note "
                     "and we’ll get back to you."),
    "end_kicker": "Let’s bloom",
    "end_h": "Have a date in mind?",
    "end_body": "Request your event and we’ll reach out to talk color, inspiration and flower requests.",
}

# Round 3 (Josh, 1 Nov): one copy set. The Kily's-voice set (round 2) was dropped; its
# hero eyebrow and story text were kept here. Round-2 source is in git history.

FOOTER_NOTE = ("Mockup for review. Photos are The Copper Tulip’s own. Logo is an interim lockup until "
               "the van logo file arrives. Fonts are stand-ins until the brand fonts are licensed for web.")

# Review notes drawn on the frame (yellow tags). --no-notes removes them for the build.
NOTES = {
    "logo": "Interim logo: closest lockup we have (cream). Swap for the light van logo file when Kily sends it.",
    "seasonal": "Live from Kily’s app (Settings → Website): she turns it on or off and sets the heading, text, photo, button text and which pre-order page the button opens.",
    "contact": "Built in Replit: each message is saved to the site and emailed to Kily, with a “got it” reply to the sender (Resend). Needs her domain and her yes on the receiving email.",
    "story": "Draft from Kily’s emails and the kickoff call. Kily and Meg to confirm or rewrite.",
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
nav{display:flex;gap:30px;font-size:13.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--green-d);margin-left:-60px}
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
.end .k{font-size:30px;color:var(--teal);margin:0 auto}
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
# Additions to the layout CSS: copy picker, links, story note, package intro, extras sub-line.
CSS2 = r"""
[hidden]{display:none!important}
.pick{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:#F1F3F5;border-bottom:1px solid #c9ced3;
 padding-block:12px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));
 display:flex;flex-direction:column;align-items:center;gap:8px;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:21;background:#F1F3F5}
.pick p{margin:0;font-size:14px;font-weight:600;color:#1d2328}
.pick .grp{display:inline-flex;border:1.5px solid #1d2328;border-radius:6px;overflow:hidden;background:#fff}
.pick button{font:600 14px/1 system-ui,-apple-system,sans-serif;color:#1d2328;background:#fff;border:0;border-left:1px solid #c9ced3;padding:10px 18px;cursor:pointer}
.pick button:first-child{border-left:0}
.pick button[aria-pressed="true"]{background:#1d2328;color:#fff}
.pick button:focus-visible{outline:3px solid #4c7ec9;outline-offset:-3px}
.rendering .pick{display:none}
nav a{color:inherit;text-decoration:none}
.step h3 a{color:inherit;text-decoration:underline;text-decoration-color:var(--peach);text-decoration-thickness:3px;text-underline-offset:5px}
.pk .intro{color:#e8efe9;font-size:18px;margin:-24px 0 36px;max-width:720px}
.exl .sub{font-size:15px;opacity:.85;margin-top:2px}
.contact{position:relative;display:grid;grid-template-columns:1fr 1.3fr;gap:64px;align-items:start;padding:20px 0 100px}
.contact h2{font-size:46px;margin-bottom:16px}.contact .ctext p{font-size:19px;margin:0}
.contact .note{position:relative;left:auto;top:auto;grid-column:1/-1;justify-self:start;margin-bottom:-36px}
.cform{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.cform label{display:flex;flex-direction:column;gap:6px;font-size:15px;font-weight:700;color:var(--green-d)}
.cform label span{font-weight:400;color:var(--body)}.cform label b{font-weight:700}
.cform input,.cform textarea{font:16px Arimo,"Liberation Sans",Arial,sans-serif;color:var(--ink);background:#fff;border:1.5px solid var(--rule);border-radius:12px;padding:12px 14px}
.cform input:focus,.cform textarea:focus{outline:none;border-color:var(--green)}
.cform .full{grid-column:1/-1}.cform .btn{cursor:pointer}
.cform .sent{margin:12px 0 0;color:var(--green-d);font-weight:700}
.story{position:relative}.story .note{left:calc(50% - var(--w)/2 + 500px);top:40px}
@media (max-width:760px){
 .pick p{font-size:13px}
 .pk .intro{font-size:16px;margin:-12px 0 24px}
 .contact{grid-template-columns:1fr;gap:24px;padding:10px 0 64px}.contact h2{font-size:32px}.contact .ctext p{font-size:17px}
 .contact .note{position:relative;top:auto;margin-bottom:6px}
 .cform{grid-template-columns:1fr}
 .story .note{position:relative;left:auto;top:auto;margin:14px 14px 0}
}
"""

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def bg(n, pos="50% 50%"):
    return f"background-image:url('{ph(n)}');background-position:{pos}"

def book(label, cls="btn"):
    return f"<a class='{cls}' href='{BOOK}' target='_blank' rel='noopener'>{esc(label)}</a>"

def variant(key, notes):
    c = COPY[key]
    o = []
    a = o.append
    k = key  # anchor suffix, so both sets can sit on one page
    banner = esc(c["banner"]).replace("@thecoppertulip", "<b>@thecoppertulip</b>")
    a(f"<div class=banner>{banner}</div><div class=sc-down></div>")
    a("<header><div class='wrap hdr'>"
      f"<a class=logo href='#top-{k}' id='top-{k}'><img src='{LOGO}' alt='The Copper Tulip, pop-up flower bar'></a>"
      f"<nav><a href='#packages-{k}'>Packages</a><a href='#how-{k}'>How it works</a>"
      f"<a href='#extras-{k}'>Extras</a><a href='#faq-{k}'>FAQ</a><a href='#contact-{k}'>Contact</a></nav>"
      f"{book(c['cta'])}</div>")
    if notes: a(f"<div class=note>{esc(NOTES['logo'])}</div>")
    a("</header>")
    # hero: photo 49 (no cart sign). 94's sign reads "gift wrapping" and stays cropped out.
    a(f"<div class=hero-wrap><section class=hero style=\"{bg(49,'50% 62%')}\"><div class=ph style=\"{bg(49,'55% 60%')}\"></div>"
      f"<div class=card><p class=eyebrow>{esc(c['hero_eyebrow'])}</p><h1>{esc(c['hero_h1'])}</h1>"
      f"<h2>{esc(c['hero_h2'])}</h2><p>{esc(c['hero_body'])}</p><div class=btns>"
      f"{book(c['cta'])}<a class='btn ghost' href='#packages-{k}'>See packages</a></div></div></section></div>")
    a("<div class=occ>" + "".join(f"<span>{esc(x)}</span>" for x in c["occasions"]) + "</div><div class=sc-down></div>")
    a(f"<section class='wrap meet' id='how-{k}'><div class=top><div><p class=eyebrow>{esc(c['meet_eyebrow'])}</p>"
      f"<h2>{esc(c['meet_h'])}</h2></div><p>{esc(c['meet_body'])}</p></div><div class=steps>")
    for i, (t, d, link) in enumerate(c["steps"], 1):
        title = f"<a href='{BOOK}' target='_blank' rel='noopener'>{esc(t)}</a>" if link else esc(t)
        a(f"<div class=step><div class=n>Step {i}</div><h3>{title}</h3><p>{esc(d)}</p></div>")
    a("</div></section>")
    a(f"<section class='wrap feat'><div class=img style=\"{bg(62,'50% 42%')}\"></div><div>"
      f"<p class=eyebrow>{esc(c['feat_eyebrow'])}</p><h2>{esc(c['feat_h'])}</h2><p>{esc(c['feat_body'])}</p></div></section>")
    a(f"<div class='sc-up pk-top'></div><section class=pk id='packages-{k}'><div class=wrap>"
      f"<p class=eyebrow>{esc(c['pk_eyebrow'])}</p><h2>{esc(c['pk_h'])}</h2>")
    if c["pk_intro"]: a(f"<p class=intro>{esc(c['pk_intro'])}</p>")
    a("<div class=pcards>")
    for p in c["packages"]:
        a(f"<div class=pc><div class=img style=\"{bg(p['photo'],p['pos'])}\"></div><div class=b>"
          f"<h3>{esc(p['name'])}</h3><div class=price>{p['price']} <small>per guest</small></div>"
          f"<p class=desc>{esc(p['desc'])}</p><ul>" + "".join(f"<li>{esc(r)}</li>" for r in p["rows"]) + "</ul>")
        if p["note"]: a(f"<p class=fav>{esc(p['note'])}</p>")
        a(f"<div class=sp></div>{book(p['btn'])}</div></div>")
    a(f"</div><p class=both>{esc(c['pk_both'])}</p></div></section><div class='sc-down pk-bot'></div>")
    a("<section class='wrap seas'>")
    if notes: a(f"<div class=note>{esc(NOTES['seasonal'])}</div>")
    a(f"<div><p class=eyebrow>{esc(c['seasonal_eyebrow'])}</p><h2>{esc(c['seasonal_h'])}</h2>"
      f"<p>{esc(c['seasonal_body'])}</p><a class=btn href='#top-{k}'>{esc(c['seasonal_btn'])}</a></div>"
      f"<div class=img style=\"{bg(77,'50% 45%')}\"></div></section>")
    # story: photo 94 cropped to the umbrella and flowers, above the cart sign.
    a(f"<div class=story-wrap><section class=story style=\"{bg(94,'50% 30%')}\"><div class=ph style=\"{bg(94,'50% 8%')}\"></div>")
    a(f"<div class=card><p class=eyebrow>{esc(c['story_eyebrow'])}</p><h2>{esc(c['story_h'])}</h2>"
      f"<p>{esc(c['story_body'])}</p></div>")
    if notes: a(f"<div class=note>{esc(NOTES['story'])}</div>")
    a("</section></div>")
    a(f"<section class=ex id='extras-{k}'><div class=wrap><p class=eyebrow>{esc(c['ex_eyebrow'])}</p><h2>{esc(c['ex_h'])}</h2><div class=exph>")
    for n, pos, alt in (( 13, "50% 45%", "Ribboned flower carriers"), (83, "50% 55%", "Arrangements"), (37, "50% 40%", "Bud vases")):
        a(f"<div role=img aria-label='{esc(alt)}' style=\"{bg(n,pos)}\"></div>")
    a("</div><div class=exl>")
    for n, pr, sub in c["extras"]:
        a(f"<div><h3>{esc(n)}</h3><p>{esc(pr)}</p>" + (f"<p class=sub>{esc(sub)}</p>" if sub else "") + "</div>")
    a("</div></div></section>")
    a(f"<section class='wrap faq' id='faq-{k}'><p class=eyebrow>{esc(c['faq_eyebrow'])}</p><h2>{esc(c['faq_h'])}</h2><div class=list>")
    for q, ans in c["faq"]:
        a(f"<div class=q><h3>{esc(q)}</h3><p>{esc(ans)}</p></div>")
    a("</div></section>")
    a(f"<section class='wrap contact' id='contact-{k}'>")
    if notes: a(f"<div class=note>{esc(NOTES['contact'])}</div>")
    a(f"<div class=ctext><p class=eyebrow>{esc(c['contact_eyebrow'])}</p><h2>{esc(c['contact_h'])}</h2>"
      f"<p>{esc(c['contact_body'])}</p></div>"
      f"<form class=cform onsubmit='event.preventDefault();this.querySelector(\".sent\").hidden=false;'>"
      f"<label>Name<input id='c-name-{k}' required autocomplete=name></label>"
      f"<label>Email<input id='c-email-{k}' type=email required autocomplete=email></label>"
      f"<label><b>Phone <span>(optional)</span></b><input id='c-phone-{k}' type=tel autocomplete=tel></label>"
      f"<label><b>Event date <span>(optional)</span></b><input id='c-date-{k}' type=date></label>"
      f"<label class=full>Message<textarea id='c-msg-{k}' rows=4 required></textarea></label>"
      f"<div class=full><button class=btn type=submit>Send message</button>"
      f"<p class=sent hidden>Thanks! Your message is on its way. (Mockup: nothing is sent.)</p></div></form></section>")
    a(f"<section class=end><p class=k>{esc(c['end_kicker'])}</p><h2>{esc(c['end_h'])}</h2>"
      f"<p>{esc(c['end_body'])}</p>{book(c['cta'])}</section>")
    a("<div class='sc-up ft-top'></div><footer><div class='wrap row'>"
      f"<img src='{LOGO}' alt=''>"
      "<div><h4>The Copper Tulip</h4><p>Pop-up flower bar</p></div>"
      "<div><h4>Follow</h4><p>@thecoppertulip · Instagram · Facebook</p></div></div></footer>")
    if notes: a(f"<div class=mk>{esc(FOOTER_NOTE)}</div>")
    return "".join(o)

PICK_JS = r"""
<script>
(function(){
 var sets=['mockup','voice'];
 function show(k){sets.forEach(function(s){document.getElementById('v-'+s).hidden=(s!==k);});
  document.querySelectorAll('.pick button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.k===k);});}
 document.querySelectorAll('.pick button').forEach(function(b){b.onclick=function(){show(b.dataset.k);
  try{history.replaceState(null,'','#'+b.dataset.k)}catch(e){location.hash=b.dataset.k}window.scrollTo(0,0);};});
 function fromHash(){var h=(location.hash||'').slice(1);if(sets.indexOf(h)>-1)show(h);}
 window.addEventListener('hashchange',fromHash);show('mockup');fromHash();
})();
</script>"""

def page(notes=True, standalone=True):
    head = ("<!doctype html><html lang=en><head><meta charset=utf-8>"
            "<meta name=viewport content='width=device-width,initial-scale=1,viewport-fit=cover'>") if standalone else ""
    o = [head + "<title>Copper Tulip Homepage Mockup</title>"
         "<meta name=\"claude:viewport-fit-sides\" content=\"cover\">"
         f"<style>{CSS}{CSS2}</style>" + ("</head><body>" if standalone else "")]
    if len(COPY) > 1: o.append("<div class=pick><p>Copper Tulip homepage · compare the copy</p><div class=grp role=group aria-label='Copy'>"
             + "".join(f"<button type=button data-k='{k}' aria-pressed='false'>{esc(COPY[k]['label'])}</button>" for k in COPY)
             + "</div></div>")
    for k in COPY:
        o.append(f"<div class=v id='v-{k}'>{variant(k, notes)}</div>")
    o.append(PICK_JS + ("</body></html>" if standalone else ""))
    return "".join(o)

async def render(html_path, out_dir):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for k in COPY:
            for name, w in (("desktop", 1440), ("mobile", 390)):
                pg = await b.new_page(viewport={"width": w, "height": 900}, device_scale_factor=2)
                await pg.goto(html_path.as_uri() + "#" + k)
                await pg.wait_for_load_state("networkidle")
                await pg.evaluate("document.documentElement.classList.add('rendering')")
                await pg.screenshot(path=str(out_dir / f"{name}-{k}.png"), full_page=True)
                await pg.close()
        await b.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--round", default="2")
    ap.add_argument("--no-notes", action="store_true")
    ap.add_argument("--artifact", help="also write an artifact copy (no html/head/body; photos/ and brand/ beside it) to this folder")
    args = ap.parse_args()
    out = ROOT / f"round-{args.round}"
    out.mkdir(exist_ok=True)
    f = out / "index.html"
    f.write_text(page(notes=not args.no_notes), encoding="utf-8")
    asyncio.run(render(f, out))
    if args.artifact:
        import re, shutil
        dst = pathlib.Path(args.artifact); (dst / "photos").mkdir(parents=True, exist_ok=True); (dst / "brand").mkdir(exist_ok=True)
        h = page(notes=not args.no_notes, standalone=False).replace("../../../photos/", "photos/").replace("../../../brand/", "brand/")
        (dst / "index.html").write_text(h, encoding="utf-8")
        for n in sorted(set(re.findall(r"photos/(20267-31TheCopperTulip\d+\.jpg)", h))):
            shutil.copy(ROOT.parent.parent / "photos" / n, dst / "photos" / n)
        shutil.copy(ROOT.parent.parent / "brand" / "lockup-cream-no-gift-wrapping.png", dst / "brand")
    print("wrote", f, "and renders")
