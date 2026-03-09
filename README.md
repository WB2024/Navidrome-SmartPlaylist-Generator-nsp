# Navidrome Smart Playlist Creator

A fully guided, interactive CLI tool for creating `.nsp` (Navidrome Smart Playlist) files — no JSON editing, no memorising field names or operator syntax.

![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Navidrome](https://img.shields.io/badge/Navidrome-Smart%20Playlists-blue?style=flat-square)

---

## Overview

[Navidrome](https://www.navidrome.org/) Smart Playlists are dynamic playlists defined as JSON objects stored in `.nsp` files. They automatically populate based on rules you define — things like "all songs I've loved from the 80s" or "high-quality tracks I haven't played recently."

This tool guides you through building those JSON rules entirely through numbered menus, handles all the formatting, and saves the finished `.nsp` file directly to your playlist directory.

---

## Features

- **Fully guided numbered menus** — no typing field names, operators, or syntax
- **Categorised field browser** — fields grouped into Track Info, File Info, Listening Stats, Library Info, and Extra Tags
- **Plain-English operator descriptions** — e.g. "Is greater than" instead of `gt`
- **Type-aware value prompts** — booleans become Yes/No, dates show format hints, numerics show contextual examples
- **Live rules summary** — shows all rules built so far after each addition
- **Nested logic** — combine rules with `all` (AND) or `any` (OR)
- **Persistent config** — remembers your playlist directory between sessions
- **Example playlists** — built-in reference examples to get you started
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
  2.  Browse example playlists
  3.  View all available fields
  4.  Set / change save directory
  5.  Exit
```

### Creating a Playlist

Choose **Create a new smart playlist** and the wizard walks you through five steps:

1. **Details** — name and optional description
2. **Rule logic** — ALL must match (AND) or ANY can match (OR), with plain-English explanation
3. **Rules** — add one or more conditions:
   - Pick a **category** from a numbered menu (Track Info, File Info, etc.)
   - Pick a **field** from a numbered list with descriptions
   - Pick an **operator** — shown in plain English, filtered to match the field's type
   - Enter a **value** — booleans become Yes/No selections, dates show format hints, numerics show contextual examples
   - A live summary panel displays all rules built so far after each addition
4. **Sort order** — choose from a numbered list; ascending/descending presented as a follow-up choice
5. **Limit** — optionally cap the number of tracks

After completing the wizard, the generated JSON is previewed and you can confirm before saving.

---

## Fields Reference

Fields are grouped into categories in the tool's menus.

### Track Info

| Field | Description | Type |
|---|---|---|
| `title` | Track title | String |
| `artist` | Artist name | String |
| `albumartist` | Album artist | String |
| `album` | Album name | String |
| `genre` | Genre | String |
| `composer` | Composer | String |
| `year` | Year of release | Numeric |
| `tracknumber` | Track number | Numeric |
| `discnumber` | Disc number | Numeric |
| `duration` | Duration (seconds) | Numeric |
| `bpm` | Beats per minute | Numeric |

### File Info

| Field | Description | Type |
|---|---|---|
| `filetype` | File type (e.g. `flac`, `mp3`, `aac`) | String |
| `filepath` | Path relative to music library root | String |
| `bitrate` | Bitrate (kbps) | Numeric |
| `bitdepth` | Bit depth | Numeric |
| `size` | File size (bytes) | Numeric |
| `channels` | Audio channels | Numeric |
| `hascoverart` | Has cover art | Boolean |

### Listening Stats

| Field | Description | Type |
|---|---|---|
| `playcount` | Times played | Numeric |
| `rating` | Rating (0–5) | Numeric |
| `loved` | Marked as loved | Boolean |
| `lastplayed` | Date last played | Date |
| `dateloved` | Date marked as loved | Date |
| `daterated` | Date rated | Date |

### Library Info

| Field | Description | Type |
|---|---|---|
| `dateadded` | Date added to library | Date |
| `datemodified` | Date file was modified | Date |
| `compilation` | Part of a compilation | Boolean |
| `library_id` | Library ID (multi-library setups) | Numeric |

### Extra Tags

| Field | Description | Type |
|---|---|---|
| `comment` | Comment tag | String |
| `lyrics` | Lyrics | String |
| `grouping` | Grouping | String |
| `discsubtitle` | Disc subtitle | String |
| `albumtype` | Album type | String |
| `albumcomment` | Album comment | String |
| `catalognumber` | Catalog number | String |

---

## Operators Reference

Operators are automatically filtered in the tool to only show the ones valid for the selected field type.

| Operator | Plain-English Label | Applies To |
|---|---|---|
| `is` | Is exactly | String, Numeric, Boolean |
| `isNot` | Is not | String, Numeric, Boolean |
| `contains` | Contains | String |
| `notContains` | Does not contain | String |
| `startsWith` | Starts with | String |
| `endsWith` | Ends with | String |
| `gt` | Is greater than | Numeric |
| `lt` | Is less than | Numeric |
| `inTheRange` | Is between (range) | Numeric, Date |
| `inTheLast` | Within the last N days | Date |
| `notInTheLast` | Not within the last N days | Date |
| `after` | After a specific date | Date |
| `before` | Before a specific date | Date |

---

## Sorting

The tool presents sort options as a numbered list. Available sort fields:

`random` · `title` · `artist` · `album` · `year` · `rating` · `playcount` · `lastplayed` · `dateadded` · `duration` · `bitrate`

Selecting **Random** shuffles the playlist on every access. All other fields prompt for Ascending or Descending direction.

In the raw JSON:
```json
"sort": "year",
"order": "desc"
```
or for shuffle:
```json
"sort": "random"
```

---

## Example Playlists

The tool includes these as built-in browsable examples (**Browse example playlists** from the main menu).

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

### 80s Favorites
Loved or highly-rated songs from the 1980s:
```json
{
  "name": "80s Favorites",
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
- The `_` character may be ignored in `contains` / `endsWith` conditions — adjust accordingly

---

## License

MIT — use freely, modify as needed.
