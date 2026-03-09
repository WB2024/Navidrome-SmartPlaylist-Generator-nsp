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

- **"This is ..." artist playlists** — Spotify-style artist-focused playlists with 20 generation methods (top rated, deep cuts, chronological, high energy, rare gems, and more) plus full customisation of sort order and limits
- **Nearly 300 ready-made presets** across 35 categories — deploy instant playlists covering essentials, discovery, moods, decades, genres, tempo, musical keys, lyrics, ReplayGain loudness, metadata completeness, and much more
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
   git clone https://github.com/WB2024/Navidrome-SmartPlaylist-Generator-nsp.git
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
  2.  Create a "This is ..." artist playlist
  3.  Deploy preset playlists
  4.  Browse example JSON
  5.  View all available fields
  6.  Set / change save directory
  7.  Exit
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

The tool supports **100+ fields** across 12 categories — every field from Navidrome's query engine (matching [Feishin&#39;s NDSongQueryFields](https://github.com/jeffvli/feishin)). Use **View all available fields** from the main menu to browse them interactively.

### Core Track Info

| Field           | Description        | Type   |
| --------------- | ------------------ | ------ |
| `title`       | Track title        | string |
| `album`       | Album name         | string |
| `artist`      | Artist name        | string |
| `albumartist` | Album artist       | string |
| `genre`       | Genre              | string |
| `composer`    | Composer           | string |
| `year`        | Year               | number |
| `track`       | Track number       | number |
| `discnumber`  | Disc number        | number |
| `duration`    | Duration (seconds) | number |
| `bpm`         | Beats per minute   | number |

### Artists & People

| Field            | Description           | Type   |
| ---------------- | --------------------- | ------ |
| `albumartists` | Album artists (multi) | string |
| `artists`      | Artists (multi)       | string |
| `arranger`     | Arranger              | string |
| `conductor`    | Conductor             | string |
| `director`     | Director              | string |
| `djmixer`      | DJ mixer              | string |
| `engineer`     | Engineer              | string |
| `lyricist`     | Lyricist              | string |
| `mixer`        | Mixer                 | string |
| `performer`    | Performer             | string |
| `producer`     | Producer              | string |
| `remixer`      | Remixer               | string |

### Album Details

| Field              | Description      | Type    |
| ------------------ | ---------------- | ------- |
| `albumcomment`   | Album comment    | string  |
| `albumtype`      | Album type       | string  |
| `albumversion`   | Album version    | string  |
| `catalognumber`  | Catalog number   | string  |
| `compilation`    | Is a compilation | boolean |
| `recordlabel`    | Record label     | string  |
| `releasecountry` | Release country  | string  |
| `releasestatus`  | Release status   | string  |
| `releasetype`    | Release type     | string  |

### File & Quality

| Field               | Description                | Type    |
| ------------------- | -------------------------- | ------- |
| `filepath`        | File path                  | string  |
| `filetype`        | File type (e.g. flac, mp3) | string  |
| `bitrate`         | Bitrate (kbps)             | number  |
| `bitdepth`        | Bit depth                  | number  |
| `size`            | File size (bytes)          | number  |
| `channels`        | Audio channels             | number  |
| `hascoverart`     | Has cover art              | boolean |
| `explicitstatus`  | Explicit status            | string  |
| `encodedby`       | Encoded by                 | string  |
| `encodersettings` | Encoder settings           | string  |

### Listening & Favorites

| Field          | Description         | Type    |
| -------------- | ------------------- | ------- |
| `playcount`  | Play count          | number  |
| `rating`     | Rating (0–5)       | number  |
| `loved`      | Is favorite / loved | boolean |
| `lastplayed` | Date last played    | date    |
| `dateloved`  | Date favorited      | date    |

### Dates

| Field             | Description           | Type |
| ----------------- | --------------------- | ---- |
| `dateadded`     | Date added to library | date |
| `datemodified`  | Date file modified    | date |
| `originaldate`  | Original release date | date |
| `originalyear`  | Original year         | date |
| `recordingdate` | Recording date        | date |
| `releasedate`   | Release date          | date |

### Text Tags

| Field            | Description    | Type   |
| ---------------- | -------------- | ------ |
| `comment`      | Comment        | string |
| `lyrics`       | Lyrics         | string |
| `grouping`     | Grouping       | string |
| `discsubtitle` | Disc subtitle  | string |
| `subtitle`     | Track subtitle | string |
| `mood`         | Mood           | string |
| `movement`     | Movement       | string |
| `movementname` | Movement name  | string |

### Numeric Tags

| Field                     | Description           | Type   |
| ------------------------- | --------------------- | ------ |
| `disctotal`             | Total discs           | number |
| `tracktotal`            | Total tracks          | number |
| `movementtotal`         | Total movements       | number |
| `r128_album_gain`       | R128 album gain       | number |
| `r128_track_gain`       | R128 track gain       | number |
| `replaygain_album_gain` | ReplayGain album gain | number |
| `replaygain_album_peak` | ReplayGain album peak | number |
| `replaygain_track_gain` | ReplayGain track gain | number |
| `replaygain_track_peak` | ReplayGain track peak | number |

### Sort Fields

| Field                | Description        | Type   |
| -------------------- | ------------------ | ------ |
| `titlesort`        | Sort name          | string |
| `albumsort`        | Sort album         | string |
| `albumartistsort`  | Sort album artist  | string |
| `albumartistssort` | Sort album artists | string |
| `artistsort`       | Sort artist        | string |
| `artistssort`      | Sort artists       | string |
| `composersort`     | Sort composer      | string |
| `lyricistsort`     | Sort lyricist      | string |

### Identifiers & Technical

| Field          | Description | Type   |
| -------------- | ----------- | ------ |
| `library_id` | Library ID  | string |
| `isrc`       | ISRC code   | string |
| `asin`       | Amazon ASIN | string |
| `barcode`    | Barcode     | string |
| `key`        | Musical key | string |
| `language`   | Language    | string |
| `license`    | License     | string |
| `media`      | Media type  | string |
| `script`     | Script      | string |
| `copyright`  | Copyright   | string |
| `website`    | Website     | string |
| `work`       | Work        | string |

### MusicBrainz IDs

| Field                       | Description      | Type   |
| --------------------------- | ---------------- | ------ |
| `mbz_album_id`            | Album ID         | string |
| `mbz_album_artist_id`     | Album Artist ID  | string |
| `mbz_artist_id`           | Artist ID        | string |
| `mbz_recording_id`        | Recording ID     | string |
| `mbz_release_group_id`    | Release Group ID | string |
| `mbz_release_track_id`    | Release Track ID | string |
| `musicbrainz_arrangerid`  | Arranger ID      | string |
| `musicbrainz_composerid`  | Composer ID      | string |
| `musicbrainz_conductorid` | Conductor ID     | string |
| `musicbrainz_directorid`  | Director ID      | string |
| `musicbrainz_discid`      | Disc ID          | string |
| `musicbrainz_djmixerid`   | DJ Mixer ID      | string |
| `musicbrainz_engineerid`  | Engineer ID      | string |
| `musicbrainz_lyricistid`  | Lyricist ID      | string |
| `musicbrainz_mixerid`     | Mixer ID         | string |
| `musicbrainz_performerid` | Performer ID     | string |
| `musicbrainz_producerid`  | Producer ID      | string |
| `musicbrainz_remixerid`   | Remixer ID       | string |
| `musicbrainz_trackid`     | Track ID         | string |
| `musicbrainz_workid`      | Work ID          | string |

### Playlist

| Field  | Description                               | Type     |
| ------ | ----------------------------------------- | -------- |
| `id` | Playlist (for in/not-in playlist filters) | playlist |

---

## Operators Reference

Operators are automatically filtered in the tool to only show the ones valid for the selected field type.

| Operator          | Plain-English Label        | Applies To                    |
| ----------------- | -------------------------- | ----------------------------- |
| `is`            | Is exactly                 | string, number, boolean, date |
| `isNot`         | Is not                     | string, number, boolean, date |
| `contains`      | Contains                   | string, number                |
| `notContains`   | Does not contain           | string, number                |
| `startsWith`    | Starts with                | string                        |
| `endsWith`      | Ends with                  | string                        |
| `gt`            | Is greater than            | number                        |
| `lt`            | Is less than               | number                        |
| `inTheRange`    | Is between (range)         | number, date                  |
| `inTheLast`     | Within the last N days     | date                          |
| `notInTheLast`  | Not within the last N days | date                          |
| `before`        | Before a date              | date                          |
| `after`         | After a date               | date                          |
| `inPlaylist`    | Is in playlist             | playlist                      |
| `notInPlaylist` | Is not in playlist         | playlist                      |

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

## Creating a "This is ..." Playlist

Inspired by Spotify's "This is ..." playlists, this feature lets you create artist-focused smart playlists with a single guided workflow — but with **far more control** over how tracks are selected, sorted, and limited.

### How It Works

Choose **Create a "This is ..." artist playlist** from the main menu, then:

1. **Enter an album artist name** — e.g. "Radiohead", "Miles Davis", "Björk"
2. **Pick a generation method** — 20 creative ways to build the playlist (see below)
3. **Customise the sort order** — accept the smart default or override with your own multi-field sort
4. **Set a track limit** — defaults to 50, but you can choose any number
5. **Name & describe** — defaults to `"This is {Artist}"` with a method-specific description
6. **Preview & save** — review the JSON and save to your playlist directory

### 20 Generation Methods

Each method applies different rules and sort logic to create a unique listening experience:

<details>
<summary><strong>🎲 Curation & Discovery</strong></summary>

- **Random selection** — A shuffled mix of everything by the artist
- **Greatest hits** — Tracks that are loved *OR* rated 4+ *OR* played 10+ times, sorted by play count
- **Deep cuts** — Skip the obvious hits — tracks from position 4 onwards on each album
- **Album openers** — Track 1 from every album, sorted chronologically
- **Album closers** — The epic final tracks (8+ on the album, 3+ minutes long)
- **Singles** — Short tracks from early in the album (under 4:30, tracks 1–3)
- **Rare gems** — High-rated tracks (4+) with low play counts (<5) — underplayed treasures
- **Unplayed** — Tracks you haven't heard yet, shuffled randomly

</details>

<details>
<summary><strong>⭐ Ratings & Stats</strong></summary>

- **Top rated** — Highest-rated tracks first
- **Most played** — Your most-spun tracks, sorted by play count
- **Recently played** — Tracks played in the last 90 days, newest plays first
- **Loved tracks only** — Just your favourited tracks, shuffled

</details>

<details>
<summary><strong>📅 Chronological</strong></summary>

- **Chronological** — Every track sorted by release year, disc, and track number
- **Reverse chronological** — Newest releases first, then by disc and track
- **Recently added** — Newest additions to your library first

</details>

<details>
<summary><strong>⏱️ Duration & Energy</strong></summary>

- **Longest tracks** — Epic deep listens sorted by duration (longest first)
- **Shortest tracks** — Quick-fire hits sorted by duration (shortest first)
- **High energy** — Highest BPM first (requires BPM tags)
- **Chill** — Lowest BPM first (requires BPM tags)

</details>

<details>
<summary><strong>🎧 Audiophile</strong></summary>

- **Lossless only** — FLAC tracks only, sorted chronologically

</details>

### Smart Defaults

Each method comes with intelligent defaults:

- **"Greatest hits"** sorts by play count descending — your most-played favourites rise to the top
- **"Deep cuts"** randomises the track order — perfect for discovering album tracks you've overlooked
- **"Chronological"** sorts by `+year,+discnumber,+track` — a complete career retrospective in release order
- **"High energy"** sorts by BPM descending — an escalating workout playlist
- **"Rare gems"** sorts by rating descending — your highest-rated underplayed tracks

You can override any default with your own custom sort (single or multi-field, with per-field ascending/descending direction).

### Why This Is Powerful

Unlike Spotify's static "This is ..." playlists:

✅ **Dynamic** — Your playlist updates automatically as you add new albums, rate tracks, or change listening habits
✅ **Customisable** — Choose *how* tracks are selected (loved tracks? deep cuts? chronological?) and sorted
✅ **Personal** — Built from *your* library, *your* ratings, *your* play history
✅ **Infinite variations** — Create multiple playlists for the same artist with different methods ("This is Radiohead — Deep Cuts", "This is Radiohead — Chronological", etc.)
✅ **Full metadata control** — Works with all the advanced Navidrome fields (BPM, ReplayGain, MusicBrainz IDs, etc.)

### Example Use Cases

- **"This is Kendrick Lamar — Greatest Hits"** — Loved or highly-rated or frequently-played tracks, sorted by play count (50 tracks)
- **"This is Aphex Twin — Chronological"** — Every track from 1985 onwards in release order (200 tracks)
- **"This is Taylor Swift — Deep Cuts"** — Album tracks from position 4+ only, randomised (100 tracks)
- **"This is Daft Punk — High Energy"** — Highest BPM tracks first for workout playlists (30 tracks)
- **"This is Joni Mitchell — Rare Gems"** — Tracks rated 4+ stars but played fewer than 5 times (25 tracks)
- **"This is The Beatles — Album Openers"** — Track 1 from every album, chronological (13 tracks)

---

## Presets

Choose **Deploy preset playlists** from the main menu to instantly save ready-made `.nsp` files.
You can deploy them one at a time (with a preview) or all at once.

There are **nearly 300 presets** across **35 categories**:

<details>
<summary><strong>Essentials</strong> (6 presets)</summary>

| Preset          | Description                                     |
| --------------- | ----------------------------------------------- |
| Recently Played | Tracks played in the last 30 days               |
| Recently Added  | Tracks added to the library in the last 30 days |
| Most Played     | Your top 100 most-played tracks of all time     |
| Never Played    | Tracks you haven't listened to yet              |
| Loved Tracks    | All your favourited tracks, newest first        |
| Top Rated       | Tracks rated 4 stars or higher                  |

</details>

<details>
<summary><strong>Discovery</strong> (6 presets)</summary>

| Preset          | Description                                                                   |
| --------------- | ----------------------------------------------------------------------------- |
| Fresh Blood     | Added in the last 7 days and never played — your unheard new arrivals        |
| Vinyl Roulette  | 50 completely random tracks — spin the wheel                                 |
| One-Hit Wonders | Tracks you've played exactly once — give them a second chance                |
| Album Openers   | Track 1 from every album — first impressions only                            |
| Fresh Favorites | Loved in the last 30 days — your latest sonic crushes                        |
| The Slow Burn   | Added over 6 months ago, played for the first time recently — late discovery |

</details>

<details>
<summary><strong>Rediscovery</strong> (5 presets)</summary>

| Preset          | Description                                                                          |
| --------------- | ------------------------------------------------------------------------------------ |
| Forgotten Gems  | Loved or highly-rated tracks you haven't played in 6+ months                         |
| Comebacks       | Played 5+ times but not in the last 6 months — old favourites gathering dust        |
| Buried Treasure | Added over a year ago and never played — lost in the stacks                         |
| Abandoned Ships | Loved once but not played in 2+ years — what happened?                              |
| Late Bloomers   | Added over a year ago, first plays in the last 3 months — finally getting attention |

</details>

<details>
<summary><strong>Moods & Vibes</strong> (10 presets)</summary>

| Preset         | Description                                                            |
| -------------- | ---------------------------------------------------------------------- |
| Long Drives    | Epic tracks over 6 minutes — settle in for the ride                   |
| Short & Sweet  | Quick hits under 3 minutes                                             |
| Deep Cuts      | Tracks 5+ on the album — beyond the singles                           |
| Slow Burners   | Tracks under 100 BPM — chill, downtempo, mellow                       |
| Bangers Only   | High-energy tracks over 140 BPM                                        |
| Night Owls     | Long, slow, deep — music for 3 AM                                     |
| Morning Coffee | Moderate tempo, not too long — ease into the day                      |
| Study Session  | Under 100 BPM and over 4 minutes — focus-friendly background music    |
| Road Trip      | 4-7 minute favourites — windows down, volume up                       |
| Dinner Party   | Mellow tempo, mid-length, well-rated — sophisticated background music |

</details>

<details>
<summary><strong>Quality & Format</strong> (11 presets)</summary>

| Preset             | Description                                                            |
| ------------------ | ---------------------------------------------------------------------- |
| FLAC Attack        | Lossless FLAC files only — audiophile approved                        |
| Hi-Res Audio       | 24-bit or higher — studio master quality                              |
| Lossy Leftovers    | Tracks under 320kbps — candidates for upgrade                         |
| Sonic Giants       | Files over 50 MB — your storage-devouring monsters                    |
| The Featherweights | Files under 2 MB — tiny but mighty                                    |
| MP3 Nostalgia      | Good old MP3 files — Napster would be proud                           |
| AAC Collection     | AAC/M4A files — the iTunes generation                                 |
| Mono Classics      | Single-channel audio — pre-stereo charm                               |
| Surround Sound     | Multi-channel tracks — more than stereo                               |
| Lo-Fi Charm        | Low bitrate but high play count — proof that quality isn't everything |
| The Audiophile     | FLAC, 24-bit, and rated 4+ — golden ears only                         |

</details>

<details>
<summary><strong>Decades</strong> (9 presets)</summary>

| Preset              | Description                                       |
| ------------------- | ------------------------------------------------- |
| 60s Classics        | Everything from 1960–1969                        |
| 70s Classics        | Everything from 1970–1979                        |
| 80s Classics        | Everything from 1980–1989                        |
| 90s Classics        | Everything from 1990–1999                        |
| 2000s Classics      | Everything from 2000–2009                        |
| 2010s Classics      | Everything from 2010–2019                        |
| Pre-1960 Vintage    | Music from before 1960 — the golden oldies       |
| 2020s Fresh         | Everything from 2020 onwards — the latest era    |
| Turn of the Century | Music from 1998-2002 — straddling the millennium |

</details>

<details>
<summary><strong>Complex / Nested</strong> (14 presets)</summary>

| Preset                | Description                                                                                    |
| --------------------- | ---------------------------------------------------------------------------------------------- |
| 80s Gold              | Loved or highly-rated tracks from the 1980s (nested logic)                                     |
| The Collector         | Played 10+ times AND (loved OR rated 4+) — your true obsessions                               |
| Guilty Pleasures      | High play count but never loved or rated — your secret shames                                 |
| Compilation Cuts      | Tracks from compilation albums you've loved or played often                                    |
| Peak Album Experience | Loved tracks from their original disc 1, ordered by album then track                           |
| The Graveyard         | Tracks added over 2 years ago, played once or never, and not loved — do they deserve to stay? |
| The Renaissance       | Not played in 6+ months but recently loved or rated — rediscovered and reborn                 |
| Genre Hopper          | Loved tracks from compilations or multi-disc sets — eclectic by nature                        |
| The Paradox           | Low-rated tracks you've played a lot OR high-rated ones you've barely touched                  |
| The Upgrade List      | Loved tracks in lossy format — candidates for a lossless upgrade                              |
| Peak Discovery        | Added in the last 90 days AND (already loved OR rated 4+) — love at first listen              |
| The Deep End          | Long tracks (7+ min), loved or highly rated, from deep in the album — sonic journeys          |
| The Full Circle       | Track 1 from albums where you've loved it AND played 5+ times — iconic opening moments        |
| The Shelf Life        | Added 1-2 years ago, played 1-3 times, not loved — the forgotten middle ground                |

</details>

<details>
<summary><strong>Eras</strong> (10 presets)</summary>

| Preset             | Description                                           |
| ------------------ | ----------------------------------------------------- |
| British Invasion   | 1963-1966 — when Britain conquered the airwaves      |
| Summer of Love     | 1967 — peace, love, and psychedelia                  |
| Punk '77           | 1977 — the year punk broke                           |
| MTV Generation     | 1981-1992 — I want my MTV                            |
| Grunge Era         | 1991-1994 — flannel shirts and distortion pedals     |
| Y2K Era            | 1999-2003 — millennium madness and nu-metal          |
| Disco Fever        | 1975-1980 — mirror balls and platform shoes          |
| New Wave           | 1978-1985 — synths, sharp suits, and angular guitars |
| Golden Age Hip-Hop | 1986-1996 — the boom-bap golden era                  |
| Britpop            | 1993-1997 — Blur vs Oasis and everything in between  |

</details>

<details>
<summary><strong>Duration</strong> (6 presets)</summary>

| Preset           | Description                                                      |
| ---------------- | ---------------------------------------------------------------- |
| Epic Odysseys    | Mammoth tracks over 10 minutes — bring snacks                   |
| Marathon Tracks  | Ultra-long tracks over 15 minutes — the ultimate endurance test |
| The Sweet Spot   | Goldilocks tracks — between 3 and 5 minutes                     |
| Micro Tracks     | Blink-and-you'll-miss-it — under 60 seconds                     |
| The Four-Twenty  | Tracks roughly 4 minutes 20 seconds long — nice                 |
| Commute Friendly | 3-7 minute tracks — perfect for the daily commute               |

</details>

<details>
<summary><strong>Tempo & Energy</strong> (6 presets)</summary>

| Preset             | Description                                    |
| ------------------ | ---------------------------------------------- |
| Comatose           | Sub-70 BPM — practically horizontal music     |
| The Heartbeat Zone | 60-80 BPM — synced to your resting heart rate |
| Walking Pace       | 90-110 BPM — perfect for a stroll             |
| Jogging Mix        | 120-140 BPM — keep that pace steady           |
| Sprint Mode        | 160+ BPM — all-out sonic assault              |
| Workout Fuel       | 120-160 BPM, 3-5 minutes — gym-ready bangers  |

</details>

<details>
<summary><strong>Stats & Data</strong> (11 presets)</summary>

| Preset                | Description                                                                 |
| --------------------- | --------------------------------------------------------------------------- |
| Heavy Rotation        | Played 20+ times — your most-spun records                                  |
| The Obsessions        | Played 50+ times — you might have a problem                                |
| The Centurion Club    | Played 100+ times — welcome to the triple-digit club                       |
| The Untouchables      | Perfect 5-star rated tracks — flawless victories                           |
| The Indifferent       | Rated exactly 3 stars — aggressively mediocre or secretly brilliant?       |
| Underrated Gems       | Rated 4+ stars but played fewer than 5 times — criminally underplayed      |
| Rising Stars          | Added in the last 90 days and already played 3+ times — instant favourites |
| Falling Stars         | Loved tracks you haven't played in over a year — falling out of favour     |
| The Loyalists         | Played recently AND loved — your ride-or-die tracks                        |
| Statistical Anomalies | Played 10+ times but rated 1 or 2 — why do you keep listening?             |
| The One Percent       | Loved AND 5-star AND played 20+ times — the absolute elite                 |

</details>

<details>
<summary><strong>Track Position</strong> (8 presets)</summary>

| Preset             | Description                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| The B-Team         | Track 2 — the eternal runner-up, always the bridesmaid                  |
| The Middle Child   | Tracks 4-7 — the overlooked middle of the album                         |
| The Lucky Seven    | Track 7 from every album — lucky number listening                       |
| Double Digits      | Track 10 and beyond — deep album territory                              |
| Track 13           | The unlucky thirteenth track — cursed bangers only                      |
| Disc Two Deep Cuts | Everything from disc 2 onwards — the stuff casual fans never reach      |
| Hidden Tracks      | Extremely high track numbers and long duration — the secret Easter eggs |
| Singles Material   | Tracks 1-3, under 4 minutes — the obvious single choices                |

</details>

<details>
<summary><strong>Seasonal</strong> (3 presets)</summary>

| Preset         | Description                                                      |
| -------------- | ---------------------------------------------------------------- |
| Summer Anthems | Upbeat, high-energy, well-loved — soundtrack to endless summers |
| Winter Warmers | Slow, long, and cozy — music for blankets and hot chocolate     |
| Rainy Day      | Melancholic tempo, mid-length — perfect for watching the rain   |

</details>

<details>
<summary><strong>Library Housekeeping</strong> (5 presets)</summary>

| Preset              | Description                                                         |
| ------------------- | ------------------------------------------------------------------- |
| Missing Artwork     | Tracks without cover art — naked albums                            |
| Recently Modified   | Files modified in the last 30 days — recently re-tagged or updated |
| Explicit Only       | Tracks marked as explicit — parental advisory                      |
| The Void            | Not rated, not loved, never played — do these tracks even exist?   |
| Digital Archaeology | Files not modified in over 5 years — digital fossils               |

</details>

<details>
<summary><strong>Albums & Collections</strong> (2 presets)</summary>

| Preset                | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| Pure Albums Only      | No compilations — original album tracks only                     |
| Compilation Discovery | Unplayed compilation tracks — hidden in the various artists pile |

</details>

<details>
<summary><strong>Weird & Wonderful</strong> (13 presets)</summary>

| Preset               | Description                                                                   |
| -------------------- | ----------------------------------------------------------------------------- |
| Earworms             | Short tracks with high play counts — catchy hooks that won't leave your head |
| Party Starters       | Fast, short, and frequently played — instant party igniters                  |
| Perfectionist's Pick | Lossless, loved, and rated 5 — the pinnacle of your collection               |
| The Completionist    | Loved, rated 5, played 10+ times, with cover art — peak curation             |
| The Time Capsule     | Original release date before 1970 — prehistoric recordings in your library   |
| New Classics         | Released 2020+ and already rated 4+ — instant modern classics                |
| Vintage Lossless     | Pre-1970 music in FLAC — old soul, pristine quality                          |
| The Growers          | Played 10+ times but still not loved — they grew on you quietly              |
| The Soundtrack       | Your loved tracks, album-ordered — the movie of your life                    |
| The Anti-Shuffle     | Your best tracks in strict chronological order — no randomness allowed       |
| Zero to Hero         | Never played but recently added — fresh arrivals awaiting their debut        |
| The Shapeshifters    | Tracks from multi-disc albums — sprawling artistic statements                |
| Format Roulette      | Non-FLAC, non-MP3 files — the weird and wonderful formats                    |

</details>

<details>
<summary><strong>Genre</strong> (22 presets)</summary>

| Preset                     | Description                                                      |
| -------------------------- | ---------------------------------------------------------------- |
| Rock Essentials            | All your rock tracks — the backbone of any collection           |
| Pop Hits                   | Pure pop — catchy, polished, irresistible                       |
| Hip-Hop & Rap              | Beats, bars, and bass — every hip-hop track in your library     |
| Electronic & EDM           | Synths, beats, and drops — the electronic spectrum              |
| Jazz Collection            | Smooth, free, bebop, fusion — all that jazz                     |
| Blues Sessions             | 12 bars of feeling — every shade of blue                        |
| Metal Mayhem               | Heavy, heavier, heaviest — all metal subgenres welcome          |
| Classical Corner           | Centuries of composed genius — from baroque to modern classical |
| Country Roads              | Twang, steel guitars, and storytelling — country & western      |
| R&B & Soul                 | Rhythm, blues, and soul — smooth grooves                        |
| Folk & Acoustic            | Stripped back, honest, raw — campfire music                     |
| Punk Rock                  | Three chords and the truth — fast, loud, attitude               |
| Reggae & Dub               | Island rhythms and bass-heavy echoes                             |
| Funk Machine               | Get up offa that thing — pure funk                              |
| Disco Nights               | Mirror balls and four-on-the-floor — disco never died           |
| Indie & Alternative        | Left of the dial — indie and alt everything                     |
| Ambient & Downtempo        | Sonic wallpaper — ambient textures and slow atmospheres         |
| Latin Flavours             | Salsa, bossa nova, reggaeton, and more — ritmo latino           |
| Soundtrack & Score         | Film scores, game soundtracks, and musical theatre               |
| World Music                | Global sounds — music from every corner of the planet           |
| Experimental & Avant-Garde | The outer limits — music that defies categorisation             |
| Gospel & Spiritual         | Hallelujah — uplifting gospel and spiritual music               |

</details>

<details>
<summary><strong>Genre Fusions</strong> (10 presets)</summary>

| Preset               | Description                                                                   |
| -------------------- | ----------------------------------------------------------------------------- |
| Loved Rock           | Rock tracks you've loved — your personal rock hall of fame                   |
| Jazz in FLAC         | Jazz the way it should be heard — lossless and warm                          |
| Top Rated Electronic | Your best electronic tracks — rated 4 or higher                              |
| Metal Marathons      | Metal tracks over 7 minutes — epic prog and doom journeys                    |
| Mellow Classics      | Classical tracks under 100 BPM — serene and peaceful                         |
| Unplayed Genres      | Never-played tracks from jazz, classical, or folk — explore your blind spots |
| Hip-Hop Classics     | Pre-2000 hip-hop — golden age bars and beats                                 |
| Pop Perfection       | Pop tracks rated 5 stars — verified bangers only                             |
| Punk Under 2 Minutes | The punkest tracks — blisteringly short, maximum energy                      |
| Epic Soundtracks     | Soundtrack tracks over 5 mins — cinematic epics                              |

</details>

<details>
<summary><strong>Mood</strong> (16 presets)</summary>

| Preset           | Description                                                          |
| ---------------- | -------------------------------------------------------------------- |
| Happy Vibes      | Tracks tagged with a happy mood — guaranteed smiles                 |
| Sad Songs        | Permission to feel — melancholy, sad, somber tracks                 |
| Energetic        | High-energy mood tags — for when you need a boost                   |
| Relaxing         | Chill, calm, peaceful — music to decompress to                      |
| Aggressive       | Raw, angry, intense — music with teeth                              |
| Romantic         | Love songs and tender feelings — set the mood                       |
| Dark & Brooding  | Gothic, moody, ominous — for your darker moments                    |
| Dreamy           | Ethereal, floating, otherworldly — music from another dimension     |
| Nostalgic        | Wistful, bittersweet, sentimental — music that takes you back       |
| Epic & Cinematic | Grand, triumphant, sweeping — your life needs a soundtrack          |
| Groovy           | Funky, groovy, rhythmic — get your head nodding                     |
| Rebellious       | Defiant, rebellious, anarchic — music that fights back              |
| Spooky           | Creepy, haunting, sinister — perfect for Halloween or 3AM listening |
| Uplifting        | Inspirational, hopeful, uplifting — music to lift your spirits      |
| Sexy             | Sultry, seductive, steamy — after-dark listening                    |
| Playful          | Quirky, whimsical, fun — music that doesn't take itself seriously   |

</details>

<details>
<summary><strong>Mood Fusions</strong> (5 presets)</summary>

| Preset             | Description                                                             |
| ------------------ | ----------------------------------------------------------------------- |
| Happy & Loved      | Tracks tagged happy that you've also loved — double the joy            |
| Sad & Highly Rated | Beautiful sadness — melancholy tracks you rated 4 or higher            |
| Dark & Heavy       | Dark mood + metal genre — the heaviest, darkest corner of your library |
| Chill Electronic   | Relaxing mood meets electronic genre — ambient beats and warm synths   |
| Moody Discoveries  | Tracks with a mood tag but never played — what vibe are you missing?   |

</details>

<details>
<summary><strong>ReplayGain & Loudness</strong> (13 presets)</summary>

| Preset                  | Description                                                                                   |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| The Loudness War        | Tracks with very low ReplayGain — mastered LOUD, brickwalled, no mercy                       |
| Whisper Quiet           | Tracks with high ReplayGain — delicately mastered, natural dynamics                          |
| Dynamic Range Kings     | Low peak values with moderate gain — well-mastered with real dynamics                        |
| Clipping Danger         | Tracks with peak at or near 1.0 — pushing the hard limits of digital audio                   |
| Hot Albums              | Albums mastered loud — low album ReplayGain means a hot master                               |
| Gentle Albums           | Albums with high positive gain — mastered with restraint and space                           |
| The Loud & Loved        | Brickwalled masters you love anyway — loudness war survivors                                 |
| Audiophile Masters      | FLAC + low peak + moderate gain + high rating — mastering perfection                         |
| R128 Normalized         | Tracks with R128 loudness normalization tags — broadcast-standard levels                     |
| Loudness Outliers       | Tracks with extreme gain values (> +10 or < -15) — the volume oddballs                       |
| Headroom Heroes         | Tracks with peak well below 1.0 — plenty of headroom, no distortion                          |
| Volume Crankers         | Very quiet tracks needing +8 dB or more gain — turn it up!                                   |
| Album vs Track Mismatch | Tracks where album gain is much different from track gain — the loud/quiet song on the album |

</details>

<details>
<summary><strong>Musical Keys</strong> (11 presets)</summary>

| Preset              | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| Key of C Major      | The people's key — bright, simple, triumphant                 |
| Key of A Minor      | The relative minor of C — moody and introspective             |
| Key of D Major      | The key of glory — Beethoven's favourite for joy              |
| Key of E Minor      | The guitar key — rock and metal's natural home                |
| Key of G Major      | Pastoral and warm — folk and country's sweet spot             |
| Key of B-flat Major | The key of jazz and brass — warm and sophisticated            |
| Minor Keys Only     | Every track in a minor key — melancholy, tension, and drama   |
| Major Keys Only     | Every track in a major key — bright, happy, resolved          |
| Sharp Keys          | Keys with sharps — bright and cutting                         |
| Flat Keys           | Keys with flats — dark, warm, and mellow                      |
| DJ Mix Ready        | Tracks with both key and BPM data — ready for harmonic mixing |

</details>

<details>
<summary><strong>Language & International</strong> (10 presets)</summary>

| Preset                 | Description                                                                    |
| ---------------------- | ------------------------------------------------------------------------------ |
| English Language       | Tracks tagged as English — lingua franca of pop                               |
| French Chansons        | Music in French — la vie en rose                                              |
| German Musik           | Tracks in German — Kraftwerk to classical lieder                              |
| Spanish Musica         | Music in Spanish — from flamenco to reggaeton                                 |
| Italian Melodia        | Tracks in Italian — opera, pop, and canzone                                   |
| Japanese Ongaku        | Music in Japanese — J-pop, J-rock, enka, and more                             |
| Korean Eumak           | Tracks in Korean — K-pop and beyond                                           |
| Portuguese Musica      | Music in Portuguese — bossa nova, fado, MPB, and sertanejo                    |
| Non-English Favourites | Loved tracks not in English — your polyglot picks                             |
| Multilingual Library   | All tracks with a language tag — discover what languages live in your library |

</details>

<details>
<summary><strong>Lyrics</strong> (9 presets)</summary>

| Preset               | Description                                                          |
| -------------------- | -------------------------------------------------------------------- |
| Has Lyrics           | Tracks with embedded lyrics — singalong ready                       |
| Lyrics Karaoke Night | Loved tracks with lyrics — your personal karaoke setlist            |
| Lyrical Love Songs   | Tracks with 'love' in the lyrics — the universal theme              |
| Lyrical Night Tracks | Songs mentioning 'night' in the lyrics — after-dark anthems         |
| Lyrical Rain Songs   | Songs with 'rain' in the lyrics — tear-stained and atmospheric      |
| Lyrical Fire         | Songs mentioning 'fire' in the lyrics — burning intensity           |
| Lyrical Dream        | Songs with 'dream' in the lyrics — subconscious songwriting         |
| Lyrical Heart Songs  | Songs mentioning 'heart' in the lyrics — pure emotion               |
| Missing Lyrics       | Loved tracks without embedded lyrics — candidates for lyric tagging |

</details>

<details>
<summary><strong>Classical & Composed</strong> (7 presets)</summary>

| Preset                 | Description                                                                 |
| ---------------------- | --------------------------------------------------------------------------- |
| Composed Works         | Tracks with a composer tag — composed, not just performed                  |
| Multi-Movement Works   | Tracks with movement data — symphonies, sonatas, suites                    |
| Grand Works            | Works with 4+ movements — the big symphonies and concertos                 |
| Conducted Performances | Tracks with a named conductor — orchestral and choral works                |
| Arranged Pieces        | Tracks with an arranger — reinterpreted and rearranged                     |
| Long Classical         | Classical tracks over 10 minutes — symphonic movements and extended pieces |
| Favourite Composers    | Composed tracks you've loved — your personal classical canon               |

</details>

<details>
<summary><strong>Production & Credits</strong> (6 presets)</summary>

| Preset             | Description                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| Producer Spotlight | Tracks with a named producer — the invisible architects of sound         |
| Remixed            | Tracks with a remixer credit — twisted, flipped, and reinvented          |
| Engineered Sound   | Tracks with an engineer credit — the unsung heroes of recording          |
| DJ Mixed           | Tracks with a DJ mixer credit — club-tested and approved                 |
| Performed By       | Tracks with a performer credit — featured performances and guests        |
| Loved Remixes      | Remixed tracks you've loved — proof that the remix can beat the original |

</details>

<details>
<summary><strong>Labels & Releases</strong> (11 presets)</summary>

| Preset            | Description                                                          |
| ----------------- | -------------------------------------------------------------------- |
| Label Browser     | Tracks with a record label tag — browse your library by label       |
| Official Releases | Tracks marked as official release status — the real deal            |
| Bootleg Corner    | Bootleg release status — raw, unofficial, underground               |
| Promotional       | Promotional releases — advance copies and promos                    |
| Singles Only      | Release type: single — the A-sides and lead tracks                  |
| EPs Only          | Release type: EP — more than a single, less than an album           |
| Live Albums       | Release type: live — captured in the moment                         |
| Made in USA       | Released in the United States                                        |
| Made in UK        | Released in the United Kingdom — birthplace of countless genres     |
| Made in Japan     | Released in Japan — the home of bonus tracks                        |
| Made in Germany   | Released in Germany — precision engineering and electronic pioneers |

</details>

<details>
<summary><strong>Album Structure</strong> (5 presets)</summary>

| Preset          | Description                                                      |
| --------------- | ---------------------------------------------------------------- |
| Short EPs       | Albums with 6 or fewer tracks — EPs and mini-albums             |
| Standard Albums | Albums with 8-14 tracks — the classic LP format                 |
| Mammoth Albums  | Albums with 20+ tracks — sprawling epics and deluxe editions    |
| Box Sets        | Releases with 3+ discs — comprehensive collections and box sets |
| Double Albums   | 2-disc releases — double albums and expanded editions           |

</details>

<details>
<summary><strong>Dates & History</strong> (7 presets)</summary>

| Preset                   | Description                                                                      |
| ------------------------ | -------------------------------------------------------------------------------- |
| Reissued Classics        | Tracks where original date is before 1990 — vintage recordings, modern releases |
| Recorded Before Released | Tracks with recording date data — vault recordings and studio session dates     |
| Brand New Releases       | Release date in the last 90 days — freshly pressed                              |
| Loved This Week          | Tracks loved in the last 7 days — this week's sonic crushes                     |
| Loved This Month         | Tracks loved in the last 30 days — this month's highlights                      |
| Yesterday's Jams         | Played in the last 24 hours — what you were vibing to yesterday                 |
| This Year's Harvest      | Added to library this year — your annual haul                                   |

</details>

<details>
<summary><strong>Comments & Tags</strong> (5 presets)</summary>

| Preset                | Description                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| Has Comments          | Tracks with something in the comment tag — little notes from the tagger |
| Subtitled Tracks      | Tracks with a subtitle — alternate versions, duets, and variations      |
| Grouped Tracks        | Tracks with a grouping tag — custom categories beyond genre             |
| Album With Commentary | Albums with a comment in the album tag — liner notes in digital form    |
| Disc Subtitled        | Tracks with disc subtitles — named discs in multi-disc releases         |

</details>

<details>
<summary><strong>Metadata Completeness</strong> (9 presets)</summary>

| Preset             | Description                                                                 |
| ------------------ | --------------------------------------------------------------------------- |
| Perfectly Tagged   | Tracks with MusicBrainz ID, cover art, genre, and year — textbook metadata |
| MusicBrainz Tagged | Tracks with a MusicBrainz recording ID — database-verified metadata        |
| No MusicBrainz ID  | Tracks missing a MusicBrainz ID — candidates for Picard tagging            |
| Missing Genre      | Tracks with no genre tag — the uncategorised wilderness                    |
| Missing Year       | Tracks with year set to 0 or missing — when were these released?           |
| Has ISRC           | Tracks with an ISRC code — internationally standardised recordings         |
| Has Barcode        | Releases with a barcode — commercially released and catalogued             |
| Catalog Numbered   | Releases with a catalog number — label-indexed and official                |
| Well-Tagged Loved  | Loved tracks with genre, year, cover art, and MB ID — your curated jewels  |

</details>

<details>
<summary><strong>Media & Encoding</strong> (6 presets)</summary>

| Preset               | Description                                                       |
| -------------------- | ----------------------------------------------------------------- |
| CD Rips              | Media type: CD — ripped from compact disc                        |
| Vinyl Rips           | Media type: Vinyl — digitised from the grooves                   |
| Digital Media        | Media type: Digital Media — born digital, no physical source     |
| Cassette Captures    | Media type: Cassette — tape hiss and warm analogue charm         |
| Encoded By You       | Tracks with an encoded-by tag — personally ripped or converted   |
| Encoder Settings Log | Tracks with encoder settings recorded — the forensic audit trail |

</details>

<details>
<summary><strong>Copyright & Licensing</strong> (3 presets)</summary>

| Preset            | Description                                                           |
| ----------------- | --------------------------------------------------------------------- |
| Copyrighted Works | Tracks with copyright info — properly attributed                     |
| Licensed Music    | Tracks with a license tag — Creative Commons, royalty-free, and more |
| Has Website       | Tracks linking to an artist or album website — direct to the source  |

</details>

<details>
<summary><strong>Title Patterns</strong> (15 presets)</summary>

| Preset                   | Description                                                               |
| ------------------------ | ------------------------------------------------------------------------- |
| Instrumental Tracks      | Titles containing 'instrumental' — no vocals, pure music                 |
| Acoustic Versions        | Titles containing 'acoustic' — stripped-back reworkings                  |
| Live Recordings          | Titles containing 'live' — captured in the moment                        |
| Demo Recordings          | Titles containing 'demo' — rough diamonds from the studio                |
| Remix Versions           | Titles or subtitles containing 'remix' — reworked for the floor          |
| Remastered Editions      | Tracks marked as remastered — polished for a new generation              |
| Bonus Tracks             | Tracks with 'bonus' in the title — the hidden extras                     |
| Extended Mixes           | Titles containing 'extended' — longer versions for deeper listening      |
| Deluxe Editions          | Album versions marked as deluxe — expanded with extras                   |
| Covers & Tributes        | Titles containing 'cover' or 'tribute' — homage tracks                   |
| Featuring Collaborations | Titles with 'feat.' or 'ft.' — collaborative moments                     |
| Numbered Sequels         | Titles containing 'Part' or 'Pt.' — serialised storytelling              |
| Interlude & Skit         | Titles containing 'interlude', 'skit', or 'intro' — the spaces between   |
| Self-Titled Tracks       | Tracks where title starts with the same text as the album — the namesake |
| Parenthetical Versions   | Titles containing parentheses — alternate versions, editions, and notes  |

</details>

<details>
<summary><strong>Filepath & Organisation</strong> (3 presets)</summary>

| Preset          | Description                                                       |
| --------------- | ----------------------------------------------------------------- |
| The A-List      | Artists starting with 'A' — top of the alphabet, top of the pile |
| The Number Ones | Tracks with numbers in the title — countable music               |
| The 'The' Bands | Artists starting with 'The' — the most common word in band names |

</details>

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
