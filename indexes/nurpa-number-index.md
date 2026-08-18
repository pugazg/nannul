# நூற்பா Number Index

This index provides human-facing navigation for the completed canonical Nannūl Tamil layer.

## Stable identifier rule

For every numbered position `n` in the nominal source range 1–462:

`nannul-` + four-digit zero-padded number

Examples:

- நூற்பா 1 → `nannul-0001`
- நூற்பா 56 → `nannul-0056`
- நூற்பா 258 → `nannul-0258`
- நூற்பா 462 → `nannul-0462`

The unnumbered சிறப்புப்பாயிரம் uses the separate identifier:

`nannul-sirappu-payiram`

## Source-gap identifiers

Two nominal positions are reserved but have no canonical Tamil text because the controlling current Project Madurai webpage does not display them:

- `nannul-0073` — source gap; see `PM147-V001`
- `nannul-0176` — source gap; see `PM147-V003`

These identifiers must not be used for reconstructed text unless an explicit audited editorial policy changes the controlling-source rule.

## Navigation by source structure

| Range | Stable IDs | Section / இயல் | Canonical file |
|---|---|---|---|
| unnumbered | `nannul-sirappu-payiram` | சிறப்புப்பாயிரம் | `text/tamil/00-sirappuppayiram.md` |
| 1–55 | `nannul-0001`–`nannul-0055` | பொதுப்பாயிரம் | `text/tamil/01-pothuppayiram/pothuppayiram-001-055.md` |
| 56–127 | `nannul-0056`–`nannul-0127` | எழுத்து இயல் | `text/tamil/02-ezhuththathikaram/02-01-ezhuththu-iyal/ezhuththu-iyal-056-127.md` |
| 128–150 | `nannul-0128`–`nannul-0150` | பதவியல் | `text/tamil/02-ezhuththathikaram/02-02-pathaviyal/pathaviyal-128-150.md` |
| 151–203 | `nannul-0151`–`nannul-0203` | உயிரீற்றுப் புணரியல் | `text/tamil/02-ezhuththathikaram/02-03-uyireetru-punariyal/uyireetru-punariyal-151-203.md` |
| 204–239 | `nannul-0204`–`nannul-0239` | மெய்யீற்றுப் புணரியல் | `text/tamil/02-ezhuththathikaram/02-04-meyyeetru-punariyal/meyyeetru-punariyal-204-239.md` |
| 240–257 | `nannul-0240`–`nannul-0257` | உருபு புணரியல் | `text/tamil/02-ezhuththathikaram/02-05-urupu-punariyal/urupu-punariyal-240-257.md` |
| 258–319 | `nannul-0258`–`nannul-0319` | பெயரியல் | `text/tamil/03-sollathikaram/03-01-peyariyal/peyariyal-258-319.md` |
| 320–351 | `nannul-0320`–`nannul-0351` | வினையியல் | `text/tamil/03-sollathikaram/03-02-vinaiyiyal/vinaiyiyal-320-351.md` |
| 352–419 | `nannul-0352`–`nannul-0419` | பொதுவியல் | `text/tamil/03-sollathikaram/03-03-pothuviyal/pothuviyal-352-419.md` |
| 420–441 | `nannul-0420`–`nannul-0441` | இடையியல் | `text/tamil/03-sollathikaram/03-04-idaiyiyal/idaiyiyal-420-441.md` |
| 442–462 | `nannul-0442`–`nannul-0462` | உரியியல் | `text/tamil/03-sollathikaram/03-05-uriyiyal/uriyiyal-442-462.md` |

## Machine-readable resolution

See:

- `structure/identifiers.yml` — identifier policy and reserved source-gap positions;
- `data/nurpa-index.json` — machine-readable segment map and deterministic expansion rule;
- `structure/sections.yml` — source-supported hierarchy and ranges.

The identifier/index layer is derived metadata. It does not alter source wording, numbering, punctuation, or canonical segmentation.
