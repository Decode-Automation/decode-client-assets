# The Copper Tulip — website build spec

Single-page marketing site for The Copper Tulip, a pop-up flower bar run by Kily Lagarde and Meg. Guests at events pick single stems from her flower cart and build their own bouquet. Written 1 Nov 2026 by Decode. **Save this file as SPEC.md in the app root before building, and keep it current.**

## Design source (match it exactly)
The design is finished. Rebuild it faithfully: same sections, order, copy, colours, spacing, photo crops and responsive behaviour. Don't redesign anything.

- **Markup and CSS to reproduce:** https://raw.githubusercontent.com/Decode-Automation/decode-client-assets/main/copper-tulip/mockups/van-layout-4/round-5-build/index.html. Download it and use its HTML structure, CSS and copy as the starting point. It is the source of truth for every word on the page. It has no review notes and no mockup footer, and the live site has neither.
- **Desktop render (1440 wide, 2x):** https://raw.githubusercontent.com/Decode-Automation/decode-client-assets/main/copper-tulip/mockups/van-layout-4/round-5-build/desktop-mockup.png
- **Mobile render (390 wide, 2x):** https://raw.githubusercontent.com/Decode-Automation/decode-client-assets/main/copper-tulip/mockups/van-layout-4/round-5-build/mobile-mockup.png
- **Reviewer's mockup, which shows open items as yellow notes:** https://claude.ai/artifact/UBV57FeZ2c9pgkNiTTheoJ. Its notes are for reviewers only and never appear on the site.

## Assets
Download into the app (for example `public/images/`) and serve them from the app. Never hot-link GitHub.
- Logo, an interim file until Kily sends the van logo: https://raw.githubusercontent.com/Decode-Automation/decode-client-assets/main/copper-tulip/brand/lockup-cream-no-gift-wrapping.png
- Photos, all Kily's own: `https://raw.githubusercontent.com/Decode-Automation/decode-client-assets/main/copper-tulip/photos/20267-31TheCopperTulip<N>.jpg` for N = 49 (hero), 55 (Classic), 73 (Designer), 62 (bouquet feature), 77 (seasonal fallback), 94 (story), 13, 83 and 37 (extras).
- Serve photos as resized WebP (about 1600 px wide for full-bleed, 800 px for cards), with the originals as fallback and lazy loading below the fold.
- **Photo 94** shows her cart sign, which reads "gift wrapping". Keep it cropped above the sign exactly as in the source: `background-position: 50% 30%` on desktop, `50% 8%` on mobile. The sign must never be visible at any width.
- **Font:** Arimo from Google Fonts (400, 700), with the fallback stack `"Liberation Sans", Arial, sans-serif`. It stands in until her brand fonts are licensed for web.

## Pages and sections
One page, `/`, in this order: social banner, header, hero, occasions strip, How it works (3 steps), bouquet feature, Packages, Seasonal, Our story, Extras, FAQ, Contact, closing "Have a date in mind?" band, footer. Plus a 404 page in the same style with a link home.

## Functions (each must be testable)
1. **Booking links.** Every "Book your event", "Book the Classic" and "Book the Designer" button, and the Step 1 title link, opens `BOOKING_URL` in a new tab. `BOOKING_URL` is one config value. Today it is https://portal.decodeautomation.com/book/copper-tulip; it will later become her own subdomain.
2. **Nav and anchors.** Packages, How it works, Extras, FAQ and Contact in the nav, and "See packages" in the hero, smooth-scroll to their sections. Section headings aren't hidden under anything. The logo scrolls to the top.
3. **Seasonal section, live from her app.** On page load, the browser fetches `GET https://portal.decodeautomation.com/api/public/website/<PORTAL_COMPANY>`. `PORTAL_COMPANY` is a config value, default `copper-tulip`. The endpoint allows CORS from any origin and is cached for 60 seconds.
   - The response is either `{show:false}` or `{show:true, heading, text, photo_url, button_text, button_url}`.
   - `show:false`, an error or a timeout over 4 seconds: the whole Seasonal section is hidden, with no gap or placeholder left behind.
   - `show:true`: the section renders with that heading, text and photo, and the button shows `button_text` and opens `button_url` in the same tab. A null `photo_url` falls back to photo 77. The "Seasonal bouquets" eyebrow stays fixed.
   - Never show the mockup's sample seasonal copy as live content.
   - To test the shown state, add `?company=demo-alpha` to the page URL. It overrides `PORTAL_COMPANY` for that page view only. Demo Alpha's Website card was switched on 1 Nov for this test. Copper Tulip's is off, so the live site shows no Seasonal section until Kily turns hers on.
4. **Contact form** ("Questions?").
   - Fields: Name (required, up to 100 characters), Email (required, valid), Phone (optional, up to 30), Event date (optional, a date), Message (required, up to 2000). Add a hidden honeypot field.
   - The form posts to the app's own `POST /api/contact`. The server validates the fields and drops any submission with the honeypot filled or sent less than 3 seconds after the page loaded, returning success-shaped but saving nothing. It rate-limits each IP to 5 submissions per hour.
   - Every valid message is saved first to the app's own Postgres table `contact_messages` (id, name, email, phone, event_date, message, created_at, ip_hash, email_status).
   - Then it is emailed through **Resend**, using Replit's Resend connector and a `RESEND_API_KEY` secret:
     - To `CONTACT_TO`. Subject: "New message from <name> — The Copper Tulip site". Body: every field, with reply-to set to the sender.
     - An automatic reply to the sender from `CONTACT_FROM`, saying "Thanks for reaching out to The Copper Tulip! We got your message and will get back to you soon."
     - The auto-reply is sent only when `CONTACT_FROM` is set. Resend can email other people only after her domain is verified.
   - If `RESEND_API_KEY` or `CONTACT_TO` is unset, or sending fails, the message stays saved, `email_status` records the failure, and the visitor still sees success. Never lose a message.
   - On success the form is replaced by "Thanks! Your message is on its way." Field errors show inline under each field.
5. **Responsive.** It matches the desktop render at 1440 and the mobile render at 390. There is no horizontal scroll from 320 to 1920 wide. The mobile layout switches at 760 px, as in the source.
6. **Basics.** Title: "The Copper Tulip — Pop-up flower bar". Meta description: "Pop-up flower bar for corporate events, employee appreciation, brand launches, showers and birthdays. Guests pick their own flowers and build their own bouquet." Open Graph image: photo 49. Include a favicon from the logo, alt text on every photo, visible keyboard focus, and support for `prefers-reduced-motion`. Add no analytics, cookie banners or pop-ups.

## Data that must persist
- `contact_messages`, in the app's own Replit Postgres database. This is the only data the site stores. It must never connect to the Decode portal's database.

## Secrets and config (no values in code)
- `RESEND_API_KEY`, `CONTACT_TO` and `CONTACT_FROM`: the Decode team adds these. Build so the site works without them; only email is skipped.
- `BOOKING_URL` and `PORTAL_COMPANY`: config, with the defaults above.

## Redirects
None. This is a new site. Her domains (thecoppertulip.com and a misspelling) aren't bought yet, and the domain is connected later.

## Out of scope
Online booking or payment (both live in her portal), a blog, more pages, editing content from the site, analytics, and a CMS.

## Open items (from Kily; don't block the build)
- Logo: the light van logo replaces the interim lockup when she sends it.
- Brand fonts: the "Fresh Flowers" font pick and web licences.
- Domain, and the receiving email for contact messages.
- Story text: Kily and Meg to confirm.
- Package names may change.
