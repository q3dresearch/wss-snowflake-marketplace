"""Parser for schema_id `sfmarketplace.v1` -- the Snowflake Marketplace sitemap.

WHAT MOVES HERE IS A DATA PRODUCT LEAVING THE MARKET

The sitemap is the only observable. Measured 2026-09-24 with a six-case control,
a live listing, a departed listing, two garbage ids, a bare path and an unrelated
path ALL returned 200 at exactly 68,372 bytes with the same SHA-256: one static
SPA shell for every URL under /marketplace/. So the detail page tells you nothing
and its status code tells you less. There is no provider field, no price, no
usage figure and no date anywhere reachable.

What the sitemap gives is an id, a name, and membership. That is enough, because
the question is which products are withdrawn from sale -- and `listed` going
absent IS the withdrawal. Across the 146 days between the 2026-05-01 archive
memento and the first capture, 354 of 3,765 listings departed (9.4%) and 628
arrived.

THE ENTITY IS THE LISTING ID, NOT THE SLUG

`GZSNZT9G` is stable; the slug is derived from a title a vendor can rename. Keying
on the slug would read a rename as a death plus a birth. The slug is emitted as
`product_slug` so a rename is visible AS a rename -- and so that a departed
listing is still identifiable, which is the one thing Databricks' bare-uuid URLs
cannot offer.

NO DENOMINATOR. Nothing here is a popularity signal. Anything built on this is an
arrivals-and-departures series and must say so.
"""
import re

from wss import derive

PARSER_VERSION = "1"
SCHEMA_ID = "sfmarketplace.v1"

# /marketplace/listing/<ID>/<slug>  -- ID is upper alnum, slug is lower kebab.
LISTING = re.compile(r"/marketplace/listing/([A-Z0-9]+)/([a-z0-9][a-z0-9-]*)")


def parse(body: bytes, ctx: derive.ParseContext):
    text = body.decode("utf-8", "replace")
    seen = set()
    for listing_id, slug in LISTING.findall(text):
        if listing_id in seen:
            # The sitemap carries a few near-duplicate entries per listing
            # (trailing-slash and query variants). Count the listing once.
            continue
        seen.add(listing_id)

        yield derive.Observation(entity_id=listing_id, metric="listed", value=1, unit="count")
        yield derive.Observation(entity_id=listing_id, metric="product_slug", value=slug)
        # The vendor prefix is the leading token of the slug for most listings
        # (lseg-starmine-..., apexanalytix-smartvm). It is a HINT, not a field
        # the publisher gives, so it is named as one and must not be treated as
        # a reliable vendor key.
        yield derive.Observation(entity_id=listing_id, metric="slug_first_token",
                                 value=slug.split("-", 1)[0])


derive.register(SCHEMA_ID, parse, PARSER_VERSION)
