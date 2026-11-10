# Data shape

*Generated 2026-11-10T12:41:50Z by `wss schema` from the derived rows. Do not hand-edit — regenerate after any derive.*

**You should not need to download anything to read this.**

- **98,622 observations** across 3 partition(s), in **1 series**
  - `snowflake.marketplace.listings` — 98,622 rows, **4381 entities**
- Raw: 8 file(s), 745,099 bytes on disk, 8 capture date(s), 2026-09-24 → 2026-11-10

## Sources

| source | cadence | endpoints | storage | personal data | licence |
| --- | --- | ---: | --- | --- | --- |
| `snowflake.marketplace.listings` | weekly | 1 | git | none | NOT ESTABLISHED (checked 2026-09-24). app.snowflake.com/robo |

## Columns

```
series_id, entity_id, observed_at, captured_at, metric, value, unit, source_id, raw_ref, parser_version
```

`entity_id` looks like: **snowflake.marketplace.listings** `GZ1M6Z10S5AI`, `GZ1M6Z10S5EE`, `GZ1M6Z1365UP`

## Metrics

| metric | series | rows | entities | type | unit | distinct | range / samples |
| --- | --- | ---: | ---: | --- | --- | ---: | --- |
| `listed` | snowflake.marketplace.listings | 32,874 | 4381 | bool | count | 1 | `1` |
| `product_slug` | snowflake.marketplace.listings | 32,874 | 4381 | text |  | 4384 | `1q-1q-us-consumer-audien`, `1q-1q-us-consumer-foot-t`, `2150-datavault-builder-a` |
| `slug_first_token` | snowflake.marketplace.listings | 32,874 | 4381 | text |  | 1068 | `1q`, `2150`, `2iq` |

## Partitions

- `derived/observations/2026-09.csv.gz`
- `derived/observations/2026-10.csv.gz`
- `derived/observations/2026-11.csv.gz`
