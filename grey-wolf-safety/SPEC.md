# Grey Wolf Safety Group — Website Build Spec

Save this file as SPEC.md in the app root before building. It is the source of truth for this build.

## What this is
A marketing front site for Grey Wolf Safety Group (Broussard, Louisiana), an industrial supplier selling 19 product categories online. Build the approved homepage design ("Direction 1 — Current Brand") plus four inner pages. The online store (catalog, search, product pages, account, cart, checkout) is NOT rebuilt: every shop-related link goes to the existing store.

## Design source
- Figma file: https://www.figma.com/design/vQ92weCyssMTOOkK9grIYB
- Desktop frame (1440 wide): https://www.figma.com/design/vQ92weCyssMTOOkK9grIYB?node-id=4-2
- Mobile frame (390 wide): https://www.figma.com/design/vQ92weCyssMTOOkK9grIYB?node-id=6-2
- If the Figma frames can't be opened, build from these renders (match layout, spacing, type and color exactly):
  - Desktop: https://raw.githubusercontent.com/Decode-Automation/decode-client-assets/main/grey-wolf-safety/mockups/round-1/direction-1-desktop.png
  - Mobile: https://raw.githubusercontent.com/Decode-Automation/decode-client-assets/main/grey-wolf-safety/mockups/round-1/direction-1-mobile.png
- Font: Manrope (Google Fonts), weights 400/500/600/700/800.
- Colors: ink #23272A, muted text #5F666B, accent green #0C9258, light panel #F1F3F4, divider #DCE0E2, dark band #23272A, footer #1A1D1F, white #FFFFFF. Buttons have 4px corners (not pill-shaped).
- Content width 1200px (120px side margins at 1440). Mobile side padding 20px.

## Client feedback applied
- Messaging is general industrial-supplier language, not safety-led. Safety & Security is one category among many.
- Client chose Direction 1, "Current Brand".

## Store links (single setting)
Create one setting STORE_BASE_URL = https://www.greywolfsafety.com and build every store link from it, so the store address can be changed in one place later.
- Search: {STORE_BASE_URL}/search?q={terms}
- Category: {STORE_BASE_URL}/{slug} (slugs below)
- Sign In: {STORE_BASE_URL}/my-account/login
- Cart: {STORE_BASE_URL}/cart
- Product links: listed under Featured products

## Images (download into the app; do not hotlink)
Base: https://raw.githubusercontent.com/Decode-Automation/decode-client-assets/main/grey-wolf-safety/build/
- Logos: logo-full.png (full color, header), logo-full-white.png (footer on dark), mark.png, mark-white.png
- Products (transparent cut-outs): product-maxiflex-glove.png, product-comfo-respirator.png, product-contractor-harness.png, product-bloodborne-kit.png, product-safety-helmet.png, product-gzero-powder.png
- Brands: brand-mechanix.png, brand-weiler.png, brand-simplegreen.png, brand-lenox.png, brand-scotch.png, brand-zep.png, brand-bline.png
- Original captured site assets (manifest): https://raw.githubusercontent.com/Decode-Automation/decode-client-assets/main/grey-wolf-safety/manifest.json — use icon-1.png (apple-touch-icon), icon-2.png and icon-3.png (favicons), icon-4.svg (pinned tab) from the same folder (…/grey-wolf-safety/).
- Icons in the design (category tiles, phone, account, cart, search, arrows, checks) are Lucide-style line icons.

## Pages
1. Home `/` — exactly the Figma frame, top to bottom:
   - Utility bar: "Service Disabled Veteran Owned Small Business · Broussard, Louisiana" · 337.451.6829 · sales@greywolfsafety.com · Contact Us
   - Header: logo · search field "Search products and brands" with green Search button · Call us 337.451.6829 · Account / Sign In · Cart
   - Nav: "Top Categories" dropdown (all 19 categories) · MRO Supplies · Welding Supplies · Power Tools · Oilfield · Safety & Security · FR · AED · About Us · Contact Us
   - Hero: eyebrow "Grey Wolf Safety Group · Broussard, Louisiana"; headline "One supplier. Every job."; subline "Abrasives to welding supplies across 19 categories, with fast, reliable, professional service to all industries throughout the continental United States."; buttons "Shop supplies" (scrolls to #categories on this page) and "Call 337.451.6829"; product composition (helmet, glove, harness on white disc) with tag "Safety Helmet, 6-point Ratchet / $20.63 /ea"
   - Trust strip: Over 30 years' experience · One supplier, 19 product categories · Serving all industries throughout the continental United States
   - Shop by category (id="categories"), 8 tiles + "All 19 categories" link (opens the full list): MRO Supplies, Welding Supplies, Power Tools, Hand Tools, Oilfield, Janitorial Equipment, Electrical & Lighting, Safety & Security
   - Why buy from Grey Wolf: eyebrow "About Grey Wolf Safety Group"; intro "Everything your crews need, from one supplier in Broussard, Louisiana."; About Us link; four points:
     - One supplier, 19 categories — From abrasives and fasteners to pumps and welding supplies.
     - Brands your crews already use — Mechanix Wear, Weiler, Lenox, Scotch, Zep Professional, Simple Green, B-LINE and Gatorade.
     - Fast, reliable, professional service — Serving all industries throughout the continental United States.
     - Over 30 years' experience — Our business development team brings over 30 years' experience.
   - Featured products (6 cards, name + price, each links to its store page), "Shop all" link to #categories
   - Featured Brands row (7 logos, each links to {STORE_BASE_URL}/search?q={brand})
   - Contact band: "Grey Wolf Safety Group is a Service Disabled Veteran Owned Small Business (SDVOSB) located in Broussard, Louisiana." · Contact Us and Call buttons · card with address, phone, email, Facebook
   - Footer: white logo · About Us · Contact Us · Privacy Policy · Terms of Use · Accessibility · Sitemap · Facebook · "© 2026 Grey Wolf Safety. All rights reserved."
2. About Us `/about-us` — same header/footer. Copy verbatim from https://www.greywolfsafety.com/about-us (Who We Are, Our Mission, Why Use Grey Wolf Safety, and the four sections). Styled with the homepage's type scale.
3. Contact Us `/contact-us` — "Contact Us"; address 1129 Evangeline Thruway (HWY 90 E), Broussard, LA 70518; phone 337.451.6829 (tap to call); email sales@greywolfsafety.com (tap to email); Facebook. No form.
4. FR `/fr-page` — carry over all content, headings, specs, the usage-guide table and product images from https://www.greywolfsafety.com/fr-page, restyled to the homepage design (no emoji in headings).
5. AED `/aed` — carry over the copy from https://www.greywolfsafety.com/aed; "Contact our office for details and pricing. 337-451-6829" as a call button.
6. Privacy Policy, Terms of Use, Accessibility: link to the existing pages at {STORE_BASE_URL}/privacy-policy, /terms-of-use, /accessibility. Sitemap: {STORE_BASE_URL}/sitemap.

## Category slugs (all 19, Top Categories dropdown and full list)
Abrasives /abrasives · Adhesives, Sealants & Tapes /adhesives-sealants-and-tapes · Chemicals, Lubricants & Paints /chemicals-lubricants-and-paints · Electrical Tools /electrical-tools · Electrical & Lighting /electrical-and-lighting · Fasteners, Clamps & Straps /fasteners-clamps-and-straps · Foodservice Supplies /foodservice-supplies · Hand Tools /hand-tools · HVAC /hvac · Janitorial Equipment /janitorial-equipment · Marking Tools /marking-tools · Material Handling /material-handling · Measuring & Leveling Tools /measuring-and-leveling-tools · MRO Supplies /mro-supplies · Oilfield /oilfield · Pneumatics /pneumatics · Power Tools /power-tools · Pumps /pumps · Welding Supplies /welding-supplies
Safety & Security: {STORE_BASE_URL}/search?index=Bution_Production_Product_Default_Bution_en-US&hierarchicalCategories%5B0%5D=Safety%20%26%20Security

## Featured products (store links)
- MaxiFlex® Cut™ Cut-Resistant Glove, Medium, Black/Green — $153.80 /DZ (12 PR/DZ) — /products/maxiflex-cut-grn-eng-yarn-blk-nit-mic-a2/en3/112-34-8743/m
- Comfo Classic® Respirator, Medium, Hycar™ Rubber — $85.58 /ea — /products/med-black-comfo-classic
- Contractor Harness, Back D-Ring, Universal Size, Quick Connect Chest and Legs — $567.11 /ca (5 ea/ca) — /products/contractor-harness-back-d-ring-universal-size-quick-connect-chest-and-legs/853-v8002210
- Bloodborne Pathogen Protection Kit, 24 Pieces, Plastic Case, Portable/Wall Mount — $45.30 /ea — /products/24-piece-bloodborne-pathogen-spill-kit
- Safety Helmet, 6-point Ratchet Suspension, Not-Vented, Green — $20.63 /ea — /products/safety-helmet-6-point-ratchet-suspension-not-vented-green
- G Zero Powder Stick, 0.10 oz Volume, 16.9 oz Yield, Grape — $95.16 /ca (120 ea/ca) — /products/g-zero-16-9-oz-powder-ks-grape

## Functions (each must pass)
1. Typing "gloves" in the header search and pressing Enter or Search opens {STORE_BASE_URL}/search?q=gloves in the same tab.
2. Every category tile, dropdown item and full-list item opens the matching store category URL.
3. Each featured product card opens its store product page.
4. Sign In opens the store login page; Cart opens the store cart.
5. Every phone number is a tap-to-call link (tel:3374516829); the email is a mailto: link.
6. "Top Categories" opens a dropdown listing all 19 categories on desktop; on mobile, the menu icon opens a full-screen menu with the same list plus About Us, Contact Us, FR and AED.
7. At 390px width the homepage matches the mobile frame: no horizontal scroll, two-column category tiles, stacked buttons.
8. /about-us, /contact-us, /fr-page and /aed load with the shared header and footer and the carried-over content.
9. Changing STORE_BASE_URL in one place updates every store link.
10. Favicons and page titles are set ("Grey Wolf Safety" plus page name).

## Data that must persist
None. The site has no forms, accounts or stored data.

## Redirects
None. Page paths match the current site (/about-us, /contact-us, /fr-page, /aed).

## Open item (not for this build)
The current store runs on www.greywolfsafety.com. Before this site takes that domain, the store needs its own address (for example shop.greywolfsafety.com), and STORE_BASE_URL is updated to it.
