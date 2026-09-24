# Data shape

*Generated 2026-09-24T12:24:43Z by `wss schema` from the derived rows. Do not hand-edit — regenerate after any derive.*

**You should not need to download anything to read this.**

- **12,117 observations** across 1 partition(s), in **1 series**
  - `snowflake.marketplace.listings` — 12,117 rows, **4039 entities**
- Raw: 1 file(s), 90,797 bytes on disk, 1 capture date(s), 2026-09-24 → 2026-09-24

## Sources

| source | cadence | endpoints | storage | personal data | licence |
| --- | --- | ---: | --- | --- | --- |
| `snowflake.marketplace.listings` | weekly | 1 | git | none | NOT ESTABLISHED (checked 2026-09-24). app.snowflake.com/robo |

## Columns

```
series_id, entity_id, observed_at, captured_at, metric, value, unit, source_id, raw_ref, parser_version
```

`entity_id` looks like: **snowflake.marketplace.listings** `GZ1M6Z10S5AI`, `GZ1M6Z1365UP`, `GZ1M6Z13LNDP`

## Metrics

| metric | series | rows | entities | type | unit | distinct | range / samples |
| --- | --- | ---: | ---: | --- | --- | ---: | --- |
| `listed` | snowflake.marketplace.listings | 4,039 | 4039 | bool | count | 1 | `1` |
| `product_slug` | snowflake.marketplace.listings | 4,039 | 4039 | text |  | 3948 | `1q-1q-us-consumer-audien`, `2150-datavault-builder-a`, `2150-datavault-builder-a` |
| `slug_first_token` | snowflake.marketplace.listings | 4,039 | 4039 | text |  | 1014 | `1q`, `2150`, `2iq` |

## Partitions

- `derived/observations/2026-09.csv.gz`
