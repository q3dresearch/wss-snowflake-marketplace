# Data shape

*Generated 2026-10-06T11:18:37Z by `wss schema` from the derived rows. Do not hand-edit — regenerate after any derive.*

**You should not need to download anything to read this.**

- **36,423 observations** across 2 partition(s), in **1 series**
  - `snowflake.marketplace.listings` — 36,423 rows, **4117 entities**
- Raw: 3 file(s), 274,043 bytes on disk, 3 capture date(s), 2026-09-24 → 2026-10-06

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
| `listed` | snowflake.marketplace.listings | 12,141 | 4117 | bool | count | 1 | `1` |
| `product_slug` | snowflake.marketplace.listings | 12,141 | 4117 | text |  | 4091 | `1q-1q-us-consumer-audien`, `2150-datavault-builder-a`, `2150-datavault-builder-a` |
| `slug_first_token` | snowflake.marketplace.listings | 12,141 | 4117 | text |  | 1030 | `1q`, `2150`, `2iq` |

## Partitions

- `derived/observations/2026-09.csv.gz`
- `derived/observations/2026-10.csv.gz`
