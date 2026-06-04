# Retail Catalog — TODO

Notes for turning `Drakkar Retail Catalog.html` into the customer-facing
version. Right now it's a byte-for-byte copy of the partner packet;
all the wholesale/internal scaffolding still needs to come out.

## Voice rule that applies

`VOICE.md` already says: **no Net 30, MOQ, terms in customer copy.**
Anything in the list below that mentions wholesale, partner, PO, MOQ,
deposit, or "internal" should not survive into this file.

---

## What to strip / change

### Cover (page 01)

- `<title>` — drop "Partner Catalog & Order Packet"
- Eyebrow "Partner Catalog & Order Packet" â†’ just "Catalog" (or drop)
- Right-side stamp "No. 001 / Wholesale" â†’ drop
- Bottom-left "Wholesale Packet Â· Spring / Summer Line Sheet" â†’ reframe
  as a customer-facing label (e.g. "Spring / Summer Catalog")
- Bottom-right "Contents" line mentions "Partner order form" — swap

### Brand story (page 02)

- Probably fine as-is. Re-read once the rest is settled.

### Catalog opener (page 03)

- Footer line: "Prices live on the internal sheet. Order sheet at the
  back." â†’ drop or replace with a "how to order" line (email, site,
  Etsy, wherever orders actually go).

### Product pages (04â€“10)

- Every pricebox: `<span class="pb-label">Wholesale</span>` â†’
  `Retail` (or just `Price`), with the actual retail dollar amount
  filled in. Retail at 2Ã— wholesale (we use keystone markup):
  A $80 Â· B $60 Â· C $120 Â· G $260 Â· M $100 Â· P $200 Â· ABC $220 Â·
  F $320 Â· N $240 Â· E $120 Â· D $220 Â· J $240 Â· H $320 Â· K $480 Â·
  Q $40 Â· TT $60 Â· PS $70.
- The MSRP sub-line under each price (`<span class="pb-note">MSRP $X</span>`)
  in the partner catalog **already shows these numbers**. For the retail
  version, swap the wholesale figure for the retail figure and drop
  the MSRP sub-line entirely.
- "Wholesale Â· Set" on the Trio Set â†’ "Retail Â· Set"
- "Wholesale Â· Featured Size" on K (Raised Bed) â†’ "Retail Â· Featured Size"
  with a "custom sizes by quote" sub-line.

### Variations & add-ons (page 11)

- Right-side italic-pull mentioning surcharges set per partner — drop.
- D Â· Bundles line: "ABC — Trio Set Â· A + B + C together at $110
  wholesale (saves $20 vs separates)." Convert to retail: "$220
  together (saves $40 vs separates)."
- D Â· Bundles line: "Custom bundles — mix any SKUs into a partner
  branded set." â†’ drop "partner branded" framing.
- C Â· Mark & brand section: the "Partner branding" / "Unbranded"
  options are partner-only — drop the whole sub-section, or trim to
  just "Drakkar maker mark — burned, on most pieces by default."
- Bottom right line: "See Partner Terms Â· page 13" — drop entirely
  (Partner Terms page will be gone in the retail version).

### Pages to delete outright

- **Page 12 — Wholesale Order Sheet** (`#p-order`). Customers don't
  fill PO numbers. Replace with a short "how to order" page if needed
  (email, lead time, where we ship), or delete and let the catalog
  end on Variations.
- **Page 13 — Partner Terms** (`#p-terms`). MOQ, Net 30, deposit,
  variation surcharges — all partner-only. Delete the whole page.
- End-of-doc link to the **Design System & Handoff** doc — that's
  internal too. Drop.

### TOC (top nav)

Remove these entries:
- Partner Order
- Partner Terms
- Design System
- Canva Build
- Handoff Brief

Rename "The Catalog" if you want; otherwise keep.

### Runners & data-screen-labels

- Page 12 runner: "Wholesale Order Sheet" â†’ gone with the page.
- Page 13 runner: "Partner Terms" â†’ gone with the page.
- Any `data-screen-label` containing "Partner" needs updating or the
  section deleting.
- `<head><title>` — drop "Partner Catalog & Order Packet".

---

## Things to add (decide before publishing)

- Where to order. Email? Website? Etsy / Faire? Pick one and put it
  on the cover footer and the back page.
- Lead time visible to customers (currently "Built to order, one at
  a time. Lead time confirmed with each order." — that's fine but
  consider a typical range, e.g. "2â€“3 weeks from order").
- Shipping / pickup info if relevant for a local Georgia customer.
- "Custom sizing by quote" — say where to send the quote request.

## Things to leave alone

- The brand story page (it's voice-correct, no wholesale framing).
- Product blurbs (already rewritten dash-free, in voice).
- Visual system: stone page, orange accents, runners, registration
  marks, monogram. All of it carries over.
- The voice — same shop, same hands, same words.
