# Data shape

*Generated 2026-10-27T09:50:43Z by `wss schema` from the derived rows. Do not hand-edit — regenerate after any derive.*

**You should not need to download anything to read this.**

- **73,692 observations** across 2 partition(s), in **1 series**
  - `snowflake.marketplace.listings` — 73,692 rows, **4312 entities**
- Raw: 6 file(s), 555,637 bytes on disk, 6 capture date(s), 2026-09-24 → 2026-10-27

## Sources

| source | cadence | endpoints | storage | personal data | licence |
| --- | --- | ---: | --- | --- | --- |
| `snowflake.marketplace.listings` | weekly | 1 | git | none | NOT ESTABLISHED (checked 2026-09-24). app.snowflake.com/robo |

## Columns

```
series_id, entity_id, observed_at, captured_at, metric, value, unit, source_id, raw_ref, parser_version
```

`entity_id` looks like: **snowflake.marketplace.listings** `GZ1M6Z10S5AI`, `GZ1M6Z1365UP`, `GZ1M6Z13LNDL`

## Metrics

| metric | series | rows | entities | type | unit | distinct | range / samples |
| --- | --- | ---: | ---: | --- | --- | ---: | --- |
| `listed` | snowflake.marketplace.listings | 24,564 | 4312 | bool | count | 1 | `1` |
| `product_slug` | snowflake.marketplace.listings | 24,564 | 4312 | text |  | 4295 | `1q-1q-us-consumer-audien`, `2150-datavault-builder-a`, `2150-datavault-builder-a` |
| `slug_first_token` | snowflake.marketplace.listings | 24,564 | 4312 | text |  | 1052 | `1q`, `2150`, `2iq` |

## Partitions

- `derived/observations/2026-09.csv.gz`
- `derived/observations/2026-10.csv.gz`
