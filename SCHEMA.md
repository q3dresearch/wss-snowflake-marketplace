# Data shape

*Generated 2026-11-03T11:58:23Z by `wss schema` from the derived rows. Do not hand-edit — regenerate after any derive.*

**You should not need to download anything to read this.**

- **86,145 observations** across 3 partition(s), in **1 series**
  - `snowflake.marketplace.listings` — 86,145 rows, **4345 entities**
- Raw: 7 file(s), 650,147 bytes on disk, 7 capture date(s), 2026-09-24 → 2026-11-03

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
| `listed` | snowflake.marketplace.listings | 28,715 | 4345 | bool | count | 1 | `1` |
| `product_slug` | snowflake.marketplace.listings | 28,715 | 4345 | text |  | 4339 | `1q-1q-us-consumer-audien`, `2150-datavault-builder-a`, `2150-datavault-builder-a` |
| `slug_first_token` | snowflake.marketplace.listings | 28,715 | 4345 | text |  | 1058 | `1q`, `2150`, `2iq` |

## Partitions

- `derived/observations/2026-09.csv.gz`
- `derived/observations/2026-10.csv.gz`
- `derived/observations/2026-11.csv.gz`
