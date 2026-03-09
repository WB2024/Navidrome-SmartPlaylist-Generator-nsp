# Navidrome Smart Playlist Creator

A fully guided, interactive CLI tool for creating `.nsp` (Navidrome Smart Playlist) files — no JSON editing, no memorising field names or operator syntax. Supports **every field and operator** that Navidrome recognises, including nested rule groups and multi-field sorting.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Navidrome](https://img.shields.io/badge/Navidrome-Smart%20Playlists-blue?style=flat-square)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-yellow?logo=buy-me-a-coffee)](https://buymeacoffee.com/succinctrecords)

---

## Overview

[Navidrome](https://www.navidrome.org/) Smart Playlists are dynamic playlists defined as JSON objects stored in `.nsp` files. They automatically populate based on rules you define — things like "all songs I've loved from the 80s" or "high-quality tracks I haven't played recently."

This tool guides you through building those JSON rules entirely through numbered menus, handles all the formatting, and saves the finished `.nsp` file directly to your playlist directory.

---

## Features

- **30+ ready-made presets** — deploy instant playlists covering essentials, discovery, moods, decades, quality, and complex nested logic
- **One-click deploy all** — save every preset at once with a single menu choice
- **100+ fields** — every field Navidrome supports, from core metadata to MusicBrainz IDs and ReplayGain values
- **Nested rule groups** — create sub-groups with their own AND/OR logic (e.g. "loved OR highly rated" inside an AND query)
- **Playlist operators** — filter by playlist membership with `inPlaylist` / `notInPlaylist`
- **Multi-field sorting** — sort by multiple fields with individual ascending/descending direction
- **Fully guided numbered menus** — no typing field names, operators, or syntax
- **12 field categories** — Core Track Info, Artists & People, Album Details, File & Quality, Listening & Favorites, Dates, Text Tags, Numeric Tags, Sort Fields, Identifiers & Technical, MusicBrainz IDs, and Playlist
- **Plain-English operator descriptions** — e.g. "Is greater than" instead of `gt`
- **Type-aware value prompts** — booleans become Yes/No, dates show format hints, numerics show contextual examples
- **Live rules summary** — shows all rules built so far after each addition
- **Persistent config** — remembers your playlist directory between sessions
- **Example playlists** — built-in reference examples including nested-logic and multi-sort
- **Beautiful UI** — enhanced display via [`rich`](https://github.com/Textualize/rich) (optional, degrades gracefully)

---

## Requirements

- Python 3.7+
- [`rich`](https://pypi.org/project/rich/) *(optional, but recommended for the best experience)*

---

## Installation

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/your-username/Navidrome-SmartPlaylist-Generator-nsp.git
   cd Navidrome-SmartPlaylist-Generator-nsp
   ```

2. **Install the optional dependency** for enhanced UI:
   ```bash
   pip install rich
   ```

3. **Run the tool:**
   ```bash
   python navidrome_smart_playlist_creator.py
   ```

---

## Usage

On first run, set your playlist directory — the folder where Navidrome scans for `.nsp` files (any subfolder inside your music library works). The path is saved and remembered for future sessions.

```
  Navidrome Smart Playlist Creator
  Generate .nsp files for Navidrome dynamic playlists

Save directory: /music/SmartPlaylists

What would you like to do?
  1.  Create a new smart playlist
  2.  Deploy preset playlists
  3.  Browse example JSON
  4.  View all available fields
  5.  Set / change save directory
  6.  Exit
```

### Creating a Playlist

Choose **Create a new smart playlist** and the wizard walks you through five steps:

1. **Rule logic** — ALL must match (AND) or ANY can match (OR), with plain-English explanation
2. **Rules** — add one or more conditions. For each rule you choose:
   - Pick a **category** (or select **Nested rule group** for sub-AND/OR logic)
   - For single rules: pick a **field** → **operator** → **value** (with full back-navigation at every step)
   - For rule groups: choose AND/OR for the sub-group, then add rules inside it (supports infinite nesting)
   - A live summary panel displays all rules built so far after each addition
3. **Sort order** — choose one or multiple sort fields; each gets its own ascending/descending direction
4. **Limit** — optionally cap the number of tracks
5. **Details** — name and optional description (asked last, so you can name it based on what you built)

After completing the wizard, the generated JSON is previewed and you can confirm before saving.

---

## Fields Reference

The tool supports **100+ fields** across 12 categories — every field from Navidrome's query engine (matching [Feishin's NDSongQueryFields](https://github.com/jeffvli/feishin)). Use **View all available fields** from the main menu to browse them interactively.

### Core Track Info

| Field | Description | Type |
|---|---|---|
| `title` | Track title | string |
| `album` | Album name | string |
| `artist` | Artist name | string |
| `albumartist` | Album artist | string |
| `genre` | Genre | string |
| `composer` | Composer | string |
| `year` | Year | number |
| `track` | Track number | number |
| `discnumber` | Disc number | number |
| `duration` | Duration (seconds) | number |
| `bpm` | Beats per minute | number |

### Artists & People

| Field | Description | Type |
|---|---|---|
| `albumartists` | Album artists (multi) | string |
| `artists` | Artists (multi) | string |
| `arranger` | Arranger | string |
| `conductor` | Conductor | string |
| `director` | Director | string |
| `djmixer` | DJ mixer | string |
| `engineer` | Engineer | string |
| `lyricist` | Lyricist | string |
| `mixer` | Mixer | string |
| `performer` | Performer | string |
| `producer` | Producer | string |
| `remixer` | Remixer | string |

### Album Details

| Field | Description | Type |
|---|---|---|
| `albumcomment` | Album comment | string |
| `albumtype` | Album type | string |
| `albumversion` | Album version | string |
| `catalognumber` | Catalog number | string |
| `compilation` | Is a compilation | boolean |
| `recordlabel` | Record label | string |
| `releasecountry` | Release country | string |
| `releasestatus` | Release status | string |
| `releasetype` | Release type | string |

### File & Quality

| Field | Description | Type |
|---|---|---|
| `filepath` | File path | string |
| `filetype` | File type (e.g. flac, mp3) | string |
| `bitrate` | Bitrate (kbps) | number |
| `bitdepth` | Bit depth | number |
| `size` | File size (bytes) | number |
| `channels` | Audio channels | number |
| `hascoverart` | Has cover art | boolean |
| `explicitstatus` | Explicit status | string |
| `encodedby` | Encoded by | string |
| `encodersettings` | Encoder settings | string |

### Listening & Favorites

| Field | Description | Type |
|---|---|---|
| `playcount` | Play count | number |
| `rating` | Rating (0–5) | number |
| `loved` | Is favorite / loved | boolean |
| `lastplayed` | Date last played | date |
| `dateloved` | Date favorited | date |

### Dates

| Field | Description | Type |
|---|---|---|
| `dateadded` | Date added to library | date |
| `datemodified` | Date file modified | date |
| `originaldate` | Original release date | date |
| `originalyear` | Original year | date |
| `recordingdate` | Recording date | date |
| `releasedate` | Release date | date |

### Text Tags

| Field | Description | Type |
|---|---|---|
| `comment` | Comment | string |
| `lyrics` | Lyrics | string |
| `grouping` | Grouping | string |
| `discsubtitle` | Disc subtitle | string |
| `subtitle` | Track subtitle | string |
| `mood` | Mood | string |
| `movement` | Movement | string |
| `movementname` | Movement name | string |

### Numeric Tags

| Field | Description | Type |
|---|---|---|
| `disctotal` | Total discs | number |
| `tracktotal` | Total tracks | number |
| `movementtotal` | Total movements | number |
| `r128_album_gain` | R128 album gain | number |
| `r128_track_gain` | R128 track gain | number |
| `replaygain_album_gain` | ReplayGain album gain | number |
| `replaygain_album_peak` | ReplayGain album peak | number |
| `replaygain_track_gain` | ReplayGain track gain | number |
| `replaygain_track_peak` | ReplayGain track peak | number |

### Sort Fields

| Field | Description | Type |
|---|---|---|
| `titlesort` | Sort name | string |
| `albumsort` | Sort album | string |
| `albumartistsort` | Sort album artist | string |
| `albumartistssort` | Sort album artists | string |
| `artistsort` | Sort artist | string |
| `artistssort` | Sort artists | string |
| `composersort` | Sort composer | string |
| `lyricistsort` | Sort lyricist | string |

### Identifiers & Technical

| Field | Description | Type |
|---|---|---|
| `library_id` | Library ID | string |
| `isrc` | ISRC code | string |
| `asin` | Amazon ASIN | string |
| `barcode` | Barcode | string |
| `key` | Musical key | string |
| `language` | Language | string |
| `license` | License | string |
| `media` | Media type | string |
| `script` | Script | string |
| `copyright` | Copyright | string |
| `website` | Website | string |
| `work` | Work | string |

### MusicBrainz IDs

| Field | Description | Type |
|---|---|---|
| `mbz_album_id` | Album ID | string |
| `mbz_album_artist_id` | Album Artist ID | string |
| `mbz_artist_id` | Artist ID | string |
| `mbz_recording_id` | Recording ID | string |
| `mbz_release_group_id` | Release Group ID | string |
| `mbz_release_track_id` | Release Track ID | string |
| `musicbrainz_arrangerid` | Arranger ID | string |
| `musicbrainz_composerid` | Composer ID | string |
| `musicbrainz_conductorid` | Conductor ID | string |
| `musicbrainz_directorid` | Director ID | string |
| `musicbrainz_discid` | Disc ID | string |
| `musicbrainz_djmixerid` | DJ Mixer ID | string |
| `musicbrainz_engineerid` | Engineer ID | string |
| `musicbrainz_lyricistid` | Lyricist ID | string |
| `musicbrainz_mixerid` | Mixer ID | string |
| `musicbrainz_performerid` | Performer ID | string |
| `musicbrainz_producerid` | Producer ID | string |
| `musicbrainz_remixerid` | Remixer ID | string |
| `musicbrainz_trackid` | Track ID | string |
| `musicbrainz_workid` | Work ID | string |

### Playlist

| Field | Description | Type |
|---|---|---|
| `id` | Playlist (for in/not-in playlist filters) | playlist |

---

## Operators Reference

Operators are automatically filtered in the tool to only show the ones valid for the selected field type.

| Operator | Plain-English Label | Applies To |
|---|---|---|
| `is` | Is exactly | string, number, boolean, date |
| `isNot` | Is not | string, number, boolean, date |
| `contains` | Contains | string, number |
| `notContains` | Does not contain | string, number |
| `startsWith` | Starts with | string |
| `endsWith` | Ends with | string |
| `gt` | Is greater than | number |
| `lt` | Is less than | number |
| `inTheRange` | Is between (range) | number, date |
| `inTheLast` | Within the last N days | date |
| `notInTheLast` | Not within the last N days | date |
| `before` | Before a date | date |
| `after` | After a date | date |
| `inPlaylist` | Is in playlist | playlist |
| `notInPlaylist` | Is not in playlist | playlist |

---

## Sorting

The tool presents common sort fields as a numbered list:

`random` · `title` · `album` · `artist` · `albumartist` · `year` · `rating` · `playcount` · `lastplayed` · `dateadded` · `duration` · `bitrate` · `genre` · `bpm` · `track` · `size`

Selecting **Random** shuffles the playlist on every access. All other fields prompt for Ascending or Descending direction.

### Multi-field sorting

After choosing a sort field and direction, the tool asks if you'd like to add another sort field. Multiple sort fields are combined with `+` (ascending) and `-` (descending) prefixes:

```json
"sort": "+artist,-year"
```

Single-field sort uses the traditional format:
```json
"sort": "year",
"order": "desc"
```

---

## Nested Rule Groups

When adding a rule, you can choose **"A rule group"** instead of a single rule. A rule group creates a nested sub-group with its own AND/OR logic inside your main query.

This is essential for complex queries like "80s Favorites" — where you need *(loved OR highly rated)* **AND** *year is 1980–1989*:

```json
{
  "all": [
    { "any": [{ "is": { "loved": true } }, { "gt": { "rating": 3 } }] },
    { "inTheRange": { "year": [1980, 1989] } }
  ]
}
```

Rule groups can be nested to any depth.

---

## Presets

Choose **Deploy preset playlists** from the main menu to instantly save ready-made `.nsp` files.
You can deploy them one at a time (with a preview) or all at once.

| Category | Preset | Description |
|---|---|---|
| **Essentials** | Recently Played | Tracks played in the last 30 days |
| | Recently Added | Added to library in the last 30 days |
| | Most Played | Top 100 most-played tracks |
| | Never Played | Unplayed tracks, randomised |
| | Loved Tracks | All favourited tracks |
| | Top Rated | Rated 4 stars or higher |
| **Discovery** | Fresh Blood | Added in last 7 days and never played |
| | Vinyl Roulette | 50 completely random tracks |
| | One-Hit Wonders | Played exactly once |
| | Album Openers | Track 1 from every album |
| **Rediscovery** | Forgotten Gems | Loved/rated but unplayed for 6+ months (nested) |
| | Comebacks | Played 5+ times but dormant for 6 months |
| | Buried Treasure | Added over a year ago, never played |
| **Moods & Vibes** | Long Drives | Tracks over 6 minutes |
| | Short & Sweet | Under 3 minutes |
| | Deep Cuts | Album track 5+ (beyond the singles) |
| | Slow Burners | Under 100 BPM |
| | Bangers Only | Over 140 BPM |
| **Quality & Format** | FLAC Attack | Lossless FLAC only |
| | Hi-Res Audio | 24-bit or higher |
| | Lossy Leftovers | Under 320 kbps — upgrade candidates |
| **Decades** | 60s–2010s Classics | One preset per decade (1960–2019) |
| **Complex / Nested** | 80s Gold | Loved or rated 4+ AND 1980s (nested) |
| | The Collector | Played 10+ AND (loved OR rated 4+) |
| | Guilty Pleasures | High plays but never loved or rated |
| | Compilation Cuts | Compilation tracks you love or play often |
| | Peak Album Experience | Loved disc-1 tracks, album order |
| | The Graveyard | 2+ years old, barely played, unloved — do they stay? |

---

## Example Playlists

The tool includes these as built-in browsable examples (**Browse example JSON** from the main menu).

### Recently Played
Tracks played in the last 30 days, most recent first:
```json
{
  "name": "Recently Played",
  "comment": "Tracks played in the last 30 days",
  "all": [{ "inTheLast": { "lastplayed": 30 } }],
  "sort": "lastplayed",
  "order": "desc",
  "limit": 100
}
```

### 80s Favorites (nested logic)
Loved or highly-rated songs from the 1980s — uses a nested `any` group inside `all`:
```json
{
  "name": "80s Favorites",
  "comment": "Loved or highly-rated songs from the 1980s",
  "all": [
    { "any": [{ "is": { "loved": true } }, { "gt": { "rating": 3 } }] },
    { "inTheRange": { "year": [1980, 1989] } }
  ],
  "sort": "year",
  "order": "desc",
  "limit": 50
}
```

### High Quality (FLAC)
Lossless FLAC files only:
```json
{
  "name": "High Quality",
  "comment": "Lossless tracks only",
  "all": [
    { "gt": { "bitrate": 900 } },
    { "is": { "filetype": "flac" } }
  ],
  "sort": "random",
  "limit": 200
}
```

### Loved Tracks
All loved tracks, newest-loved first:
```json
{
  "name": "Loved",
  "all": [{ "is": { "loved": true } }],
  "sort": "dateloved",
  "order": "desc",
  "limit": 500
}
```

### Never Played
Tracks you haven't listened to yet:
```json
{
  "name": "Never Played",
  "comment": "Tracks you haven't played yet",
  "all": [{ "is": { "playcount": 0 } }],
  "sort": "random",
  "limit": 200
}
```

### Multi-sort Example
Sorted by artist ascending, then year descending:
```json
{
  "name": "By Artist then Year",
  "comment": "Sorted by artist ascending, then year descending",
  "all": [{ "gt": { "playcount": -1 } }],
  "sort": "+artist,-year"
}
```

---

## How Navidrome Imports Playlists

Place your `.nsp` files anywhere inside your music library folder. Navidrome walks the entire music directory during a scan and imports any `.nsp` files it finds.

> **Recommended:** Create a `SmartPlaylists/` subfolder inside your music library root and save all `.nsp` files there to keep them tidy.

Navidrome automatically detects and imports them on the next library scan. Smart Playlists refresh automatically when accessed, with a minimum delay configurable via `SmartPlaylistRefreshDelay` (default: `5s`).

> **Note:** If you use a separate `PlaylistsPath` Docker volume, the internal scanner may not discover it depending on your Navidrome version. Placing `.nsp` files directly inside your music library is the most reliable approach.

---

## Configuration

The tool saves your playlist directory to `~/.navidrome_playlist_config.json` so you don't have to re-enter it each session. To change it, choose **Set / change save directory** from the main menu.

---

## Notes

- Dates must be in `YYYY-MM-DD` format — the tool shows this hint automatically
- Boolean fields (`loved`, `hascoverart`, `compilation`) are presented as Yes/No selections — no typing required
- `filepath` is relative to your music library root (no leading `/music` prefix)
- `library_id` is a string type (not numeric) — enter the ID as text
- Track number field is `track` (not `tracknumber`)
- Playlist operators (`inPlaylist` / `notInPlaylist`) require the playlist ID from Navidrome (found in the URL: `/playlists/<ID>`)

---

## License

MIT — use freely, modify as needed.
