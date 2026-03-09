#!/usr/bin/env python3
"""
Navidrome Smart Playlist Creator
A guided CLI tool to create .nsp files for Navidrome smart playlists
"""

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Confirm, Prompt
    from rich.rule import Rule
    from rich.table import Table
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("Note: Install 'rich' for a better experience: pip install rich")


def strip_markup(text: str) -> str:
    return re.sub(r'\[/?[^\]]*\]', '', text)


class SmartPlaylistCreator:
    def __init__(self):
        self.console = Console() if RICH_AVAILABLE else None
        self.config_file = Path.home() / ".navidrome_playlist_config.json"
        self.playlist_dir = self.load_config()

        # Complete field list matching Navidrome / Feishin NDSongQueryFields
        # (field_key, description, type)
        self.fields: Dict[str, List[Tuple[str, str, str]]] = {
            "Core Track Info": [
                ("title",        "Track title",            "string"),
                ("album",        "Album name",             "string"),
                ("artist",       "Artist name",            "string"),
                ("albumartist",  "Album artist",           "string"),
                ("genre",        "Genre",                  "string"),
                ("composer",     "Composer",               "string"),
                ("year",         "Year",                   "number"),
                ("track",        "Track number",           "number"),
                ("discnumber",   "Disc number",            "number"),
                ("duration",     "Duration (seconds)",     "number"),
                ("bpm",          "Beats per minute",       "number"),
            ],
            "Artists & People": [
                ("albumartists", "Album artists (multi)",  "string"),
                ("artists",      "Artists (multi)",        "string"),
                ("arranger",     "Arranger",               "string"),
                ("conductor",    "Conductor",              "string"),
                ("director",     "Director",               "string"),
                ("djmixer",      "DJ mixer",               "string"),
                ("engineer",     "Engineer",               "string"),
                ("lyricist",     "Lyricist",               "string"),
                ("mixer",        "Mixer",                  "string"),
                ("performer",    "Performer",              "string"),
                ("producer",     "Producer",               "string"),
                ("remixer",      "Remixer",                "string"),
            ],
            "Album Details": [
                ("albumcomment",    "Album comment",       "string"),
                ("albumtype",       "Album type",          "string"),
                ("albumversion",    "Album version",       "string"),
                ("catalognumber",   "Catalog number",      "string"),
                ("compilation",     "Is a compilation",    "boolean"),
                ("recordlabel",     "Record label",        "string"),
                ("releasecountry",  "Release country",     "string"),
                ("releasestatus",   "Release status",      "string"),
                ("releasetype",     "Release type",        "string"),
            ],
            "File & Quality": [
                ("filepath",         "File path",                     "string"),
                ("filetype",         "File type (e.g. flac, mp3)",    "string"),
                ("bitrate",          "Bitrate (kbps)",                "number"),
                ("bitdepth",         "Bit depth",                     "number"),
                ("size",             "File size (bytes)",             "number"),
                ("channels",         "Audio channels",                "number"),
                ("hascoverart",      "Has cover art",                 "boolean"),
                ("explicitstatus",   "Explicit status",               "string"),
                ("encodedby",        "Encoded by",                    "string"),
                ("encodersettings",  "Encoder settings",              "string"),
            ],
            "Listening & Favorites": [
                ("playcount",  "Play count",            "number"),
                ("rating",     "Rating (0-5)",          "number"),
                ("loved",      "Is favorite / loved",   "boolean"),
                ("lastplayed", "Date last played",      "date"),
                ("dateloved",  "Date favorited",        "date"),
            ],
            "Dates": [
                ("dateadded",      "Date added to library",     "date"),
                ("datemodified",   "Date file modified",        "date"),
                ("originaldate",   "Original release date",     "date"),
                ("originalyear",   "Original year",             "date"),
                ("recordingdate",  "Recording date",            "date"),
                ("releasedate",    "Release date",              "date"),
            ],
            "Text Tags": [
                ("comment",       "Comment",           "string"),
                ("lyrics",        "Lyrics",            "string"),
                ("grouping",      "Grouping",          "string"),
                ("discsubtitle",  "Disc subtitle",     "string"),
                ("subtitle",      "Track subtitle",    "string"),
                ("mood",          "Mood",              "string"),
                ("movement",      "Movement",          "string"),
                ("movementname",  "Movement name",     "string"),
            ],
            "Numeric Tags": [
                ("disctotal",              "Total discs",              "number"),
                ("tracktotal",             "Total tracks",             "number"),
                ("movementtotal",          "Total movements",          "number"),
                ("r128_album_gain",        "R128 album gain",          "number"),
                ("r128_track_gain",        "R128 track gain",          "number"),
                ("replaygain_album_gain",  "ReplayGain album gain",    "number"),
                ("replaygain_album_peak",  "ReplayGain album peak",    "number"),
                ("replaygain_track_gain",  "ReplayGain track gain",    "number"),
                ("replaygain_track_peak",  "ReplayGain track peak",    "number"),
            ],
            "Sort Fields": [
                ("titlesort",          "Sort name",            "string"),
                ("albumsort",          "Sort album",           "string"),
                ("albumartistsort",    "Sort album artist",    "string"),
                ("albumartistssort",   "Sort album artists",   "string"),
                ("artistsort",         "Sort artist",          "string"),
                ("artistssort",        "Sort artists",         "string"),
                ("composersort",       "Sort composer",        "string"),
                ("lyricistsort",       "Sort lyricist",        "string"),
            ],
            "Identifiers & Technical": [
                ("library_id",  "Library ID",          "string"),
                ("isrc",        "ISRC code",           "string"),
                ("asin",        "Amazon ASIN",         "string"),
                ("barcode",     "Barcode",             "string"),
                ("key",         "Musical key",         "string"),
                ("language",    "Language",             "string"),
                ("license",     "License",             "string"),
                ("media",       "Media type",          "string"),
                ("script",      "Script",              "string"),
                ("copyright",   "Copyright",           "string"),
                ("website",     "Website",             "string"),
                ("work",        "Work",                "string"),
            ],
            "MusicBrainz IDs": [
                ("mbz_album_id",              "Album ID",           "string"),
                ("mbz_album_artist_id",       "Album Artist ID",    "string"),
                ("mbz_artist_id",             "Artist ID",          "string"),
                ("mbz_recording_id",          "Recording ID",       "string"),
                ("mbz_release_group_id",      "Release Group ID",   "string"),
                ("mbz_release_track_id",      "Release Track ID",   "string"),
                ("musicbrainz_arrangerid",    "Arranger ID",        "string"),
                ("musicbrainz_composerid",    "Composer ID",        "string"),
                ("musicbrainz_conductorid",   "Conductor ID",       "string"),
                ("musicbrainz_directorid",    "Director ID",        "string"),
                ("musicbrainz_discid",        "Disc ID",            "string"),
                ("musicbrainz_djmixerid",     "DJ Mixer ID",        "string"),
                ("musicbrainz_engineerid",    "Engineer ID",        "string"),
                ("musicbrainz_lyricistid",    "Lyricist ID",        "string"),
                ("musicbrainz_mixerid",       "Mixer ID",           "string"),
                ("musicbrainz_performerid",   "Performer ID",       "string"),
                ("musicbrainz_producerid",    "Producer ID",        "string"),
                ("musicbrainz_remixerid",     "Remixer ID",         "string"),
                ("musicbrainz_trackid",       "Track ID",           "string"),
                ("musicbrainz_workid",        "Work ID",            "string"),
            ],
            "Playlist": [
                ("id", "Playlist (for in/not-in playlist filters)", "playlist"),
            ],
        }

        self.operators: Dict[str, List[Tuple[str, str]]] = {
            "string": [
                ("is",           "Is exactly"),
                ("isNot",        "Is not"),
                ("contains",     "Contains"),
                ("notContains",  "Does not contain"),
                ("startsWith",   "Starts with"),
                ("endsWith",     "Ends with"),
            ],
            "number": [
                ("is",           "Is exactly"),
                ("isNot",        "Is not"),
                ("contains",     "Contains"),
                ("notContains",  "Does not contain"),
                ("gt",           "Is greater than"),
                ("lt",           "Is less than"),
                ("inTheRange",   "Is between (range)"),
            ],
            "boolean": [
                ("is",    "Is"),
                ("isNot", "Is not"),
            ],
            "date": [
                ("is",            "Is exactly (date)"),
                ("isNot",         "Is not (date)"),
                ("before",        "Before a date"),
                ("after",         "After a date"),
                ("inTheLast",     "Within the last N days"),
                ("notInTheLast",  "Not within the last N days"),
                ("inTheRange",    "Between two dates"),
            ],
            "playlist": [
                ("inPlaylist",     "Is in playlist"),
                ("notInPlaylist",  "Is not in playlist"),
            ],
        }

        self.sort_options: List[Tuple[str, str]] = [
            ("random",      "Random (shuffle)"),
            ("title",       "Title"),
            ("album",       "Album"),
            ("artist",      "Artist"),
            ("albumartist", "Album Artist"),
            ("year",        "Year"),
            ("rating",      "Rating"),
            ("playcount",   "Play Count"),
            ("lastplayed",  "Last Played"),
            ("dateadded",   "Date Added"),
            ("duration",    "Duration"),
            ("bitrate",     "Bitrate"),
            ("genre",       "Genre"),
            ("bpm",         "BPM"),
            ("track",       "Track Number"),
            ("size",        "File Size"),
        ]

    # ── Output helpers ────────────────────────────────────────────────────────

    def out(self, text: str = "", style: str = "") -> None:
        if RICH_AVAILABLE and self.console:
            self.console.print(text, style=style)
        else:
            print(strip_markup(text))

    def rule(self, title: str = "") -> None:
        if RICH_AVAILABLE and self.console:
            self.console.print(Rule(f" {title} " if title else "", style="cyan"))
        else:
            print(f"\n{'─' * 60}")
            if title:
                print(f"  {title}")

    def banner(self) -> None:
        if RICH_AVAILABLE and self.console:
            self.console.print(Panel(
                "[bold cyan]Navidrome Smart Playlist Creator[/bold cyan]\n"
                "[dim]Generate .nsp files for Navidrome dynamic playlists[/dim]",
                border_style="cyan",
                padding=(1, 4),
            ))
        else:
            print("\n" + "=" * 60)
            print("  NAVIDROME SMART PLAYLIST CREATOR")
            print("=" * 60)

    def panel(self, content: str, title: str = "") -> None:
        if RICH_AVAILABLE and self.console:
            self.console.print(Panel(
                content,
                title=f"[bold cyan]{title}[/bold cyan]" if title else "",
                border_style="cyan",
                padding=(1, 2),
            ))
        else:
            print(f"\n{'=' * 60}")
            if title:
                print(f"  {strip_markup(title)}")
                print('=' * 60)
            print(strip_markup(content))
            print('=' * 60)

    def prompt(self, question: str, default: str = "") -> str:
        if RICH_AVAILABLE and self.console:
            return Prompt.ask(f"[bold]{question}[/bold]", default=default, console=self.console)
        suffix = f" [{default}]" if default else ""
        ans = input(f"{strip_markup(question)}{suffix}: ").strip()
        return ans if ans else default

    def confirm(self, question: str, default: bool = True) -> bool:
        if RICH_AVAILABLE and self.console:
            return Confirm.ask(f"[bold]{question}[/bold]", default=default, console=self.console)
        suffix = "Y/n" if default else "y/N"
        ans = input(f"{strip_markup(question)} [{suffix}]: ").strip().lower()
        return default if not ans else ans in ("y", "yes")

    def select_option(
        self,
        title: str,
        options: List[Tuple[Any, str]],
        allow_back: bool = False,
    ) -> Optional[Any]:
        """Show a numbered menu and return the chosen value, or None if user chose back."""
        while True:
            self.out()
            if RICH_AVAILABLE and self.console:
                self.console.print(f"[bold]{title}[/bold]")
                t = Table(show_header=False, box=None, padding=(0, 1, 0, 2))
                t.add_column(style="bold cyan", no_wrap=True, width=5)
                t.add_column()
                for i, (_, label) in enumerate(options, 1):
                    t.add_row(f"{i}.", label)
                if allow_back:
                    t.add_row("0.", "[dim]<- Cancel / Go back[/dim]")
                self.console.print(t)
            else:
                print(f"\n{strip_markup(title)}")
                for i, (_, label) in enumerate(options, 1):
                    print(f"  {i}. {strip_markup(label)}")
                if allow_back:
                    print("  0. <- Cancel / Go back")

            raw = self.prompt("Select", default="1")
            try:
                n = int(raw)
                if allow_back and n == 0:
                    return None
                if 1 <= n <= len(options):
                    return options[n - 1][0]
            except ValueError:
                pass
            self.out("[red]Invalid choice — please enter a number from the list.[/red]")

    # ── Config ────────────────────────────────────────────────────────────────

    def load_config(self) -> Optional[Path]:
        if self.config_file.exists():
            try:
                with open(self.config_file, "r") as f:
                    val = json.load(f).get("playlist_directory", "")
                    return Path(val) if val else None
            except Exception:
                pass
        return None

    def save_config(self, path: Path) -> None:
        with open(self.config_file, "w") as f:
            json.dump({"playlist_directory": str(path)}, f)

    def set_playlist_directory(self) -> None:
        self.rule("Save Directory")
        self.out(
            "\nThis is where your [cyan].nsp[/cyan] files will be written.\n"
            "It must be a folder that Navidrome can scan (inside your music library).\n"
        )
        if self.playlist_dir:
            self.out(f"[green]Current:[/green] {self.playlist_dir}\n")
            if not self.confirm("Change directory?", default=False):
                return

        while True:
            raw = self.prompt("Enter path")
            if not raw:
                self.out("[red]Path cannot be empty.[/red]")
                continue
            path = Path(raw).expanduser()
            if not path.exists():
                if self.confirm("Directory does not exist. Create it?", default=True):
                    try:
                        path.mkdir(parents=True, exist_ok=True)
                        self.out(f"[green]Created:[/green] {path}")
                    except Exception as e:
                        self.out(f"[red]Could not create directory: {e}[/red]")
                        continue
                else:
                    continue
            if not path.is_dir():
                self.out("[red]That path exists but is not a directory.[/red]")
                continue
            self.playlist_dir = path
            self.save_config(path)
            self.out(f"[green]Saved:[/green] {path}")
            break

    # ── Helpers ────────────────────────────────────────────────────────────────

    @staticmethod
    def _parse_number(raw: str) -> Any:
        """Parse as int if possible, otherwise float."""
        try:
            return int(raw)
        except ValueError:
            return float(raw)

    # ── Condition builder ─────────────────────────────────────────────────────

    def build_condition(self, depth: int = 0) -> Optional[Dict[str, Any]]:
        """Guide the user through building one rule or nested rule group.

        Back-navigation: cancel at field → back to category,
        cancel at operator → back to field, cancel at category → return None.
        """
        self.rule(f"{'Sub-' * depth}Add a Rule")

        while True:  # ── Category loop (back here = cancel to caller)
            cat_options: List[Tuple[str, str]] = [(c, c) for c in self.fields]
            cat_options.append(
                ("__group__", "[bold magenta]+ Nested rule group[/bold magenta]  [dim](sub-AND/OR)[/dim]")
            )
            category = self.select_option(
                "Choose a field category:",
                cat_options,
                allow_back=True,
            )
            if category is None:
                return None

            if category == "__group__":
                result = self._build_rule_group(depth + 1)
                if result is not None:
                    return result
                continue  # group cancelled → back to category list

            # ── Field loop (back → re-show categories)
            while True:
                field_entries = self.fields[str(category)]
                f_options: List[Tuple[str, str]] = [
                    (key, f"{desc}  [dim]({ftype})[/dim]")
                    for key, desc, ftype in field_entries
                ]
                field_key = self.select_option(
                    f"Choose a field  [dim][{category}][/dim]:",
                    f_options,
                    allow_back=True,
                )
                if field_key is None:
                    break  # back to category
                field_key = str(field_key)

                _, field_label, field_type = next(
                    (k, d, t) for k, d, t in field_entries if k == field_key
                )
                self.out(f"\n  [cyan]Field:[/cyan] {field_label}  [dim]({field_type})[/dim]")

                # ── Operator loop (back → re-show fields)
                while True:
                    op_entries = self.operators.get(field_type, self.operators["string"])
                    operator = self.select_option(
                        "Choose a condition:",
                        list(op_entries),
                        allow_back=True,
                    )
                    if operator is None:
                        break  # back to field
                    operator = str(operator)
                    op_label = next(d for k, d in op_entries if k == operator)
                    self.out(f"  [cyan]Condition:[/cyan] {field_label} -> {op_label}")

                    # ── Value (always completes)
                    value = self._prompt_value(field_key, field_label, field_type, operator)

                    condition = {operator: {field_key: value}}
                    self.out(f"\n[bold green]Rule added:[/bold green] [dim]{json.dumps(condition)}[/dim]")
                    return condition

                # Operator cancelled → back to field list
                continue

            # Field cancelled → back to category list
            continue

    def _build_rule_group(self, depth: int = 1) -> Optional[Dict[str, Any]]:
        """Build a nested rule group (sub-group with its own AND/OR logic)."""
        self.out(
            "\n[dim]A rule group lets you nest rules with their own AND/OR logic.\n"
            "For example: (artist is 'X' OR artist is 'Y') as part of a larger AND query.[/dim]\n"
        )
        logic = self.select_option(
            "Logic for this sub-group:",
            [
                ("all", "[bold]ALL[/bold] must match   [dim](AND)[/dim]"),
                ("any", "[bold]ANY[/bold] can match    [dim](OR)[/dim]"),
            ],
            allow_back=True,
        )
        if logic is None:
            return None
        logic = str(logic)

        conditions: List[Dict[str, Any]] = []
        while True:
            condition = self.build_condition(depth)
            if condition:
                conditions.append(condition)
                self._show_conditions_summary(conditions, logic)
                if not self.confirm("Add another rule to this sub-group?", default=False):
                    break
            elif not conditions:
                # No rules yet and user cancelled — offer escape
                if not self.confirm("No rules added yet. Keep building this group?", default=True):
                    return None
            # else: cancelled while having rules — silently loop back

        if not conditions:
            return None
        return {logic: conditions}

    def _prompt_value(self, field: str, label: str, ftype: str, operator: str) -> Any:
        """Prompt for a value with type-appropriate guidance."""

        if ftype == "boolean":
            result = self.select_option(
                f"Value for \"{label}\":",
                [("__true__", "Yes / True"), ("__false__", "No / False")],
            )
            return result == "__true__"

        if ftype == "playlist":
            self.out(
                "[dim]Enter the playlist ID from Navidrome.\n"
                "You can find it in the URL when viewing a playlist: /playlists/<ID>[/dim]"
            )
            return self.prompt("Playlist ID")

        if operator in ("inTheLast", "notInTheLast"):
            self.out("[dim]How many days back?  (e.g. 7 = last week · 30 = last month · 365 = last year)[/dim]")
            while True:
                raw = self.prompt("Days", default="30")
                try:
                    return int(raw)
                except ValueError:
                    self.out("[red]Please enter a whole number.[/red]")

        if operator == "inTheRange" and ftype == "number":
            self.out(f"[dim]Enter the start and end values for \"{label}\".[/dim]")
            while True:
                try:
                    return [self._parse_number(self.prompt("From")),
                            self._parse_number(self.prompt("To"))]
                except ValueError:
                    self.out("[red]Please enter valid numbers.[/red]")

        if operator == "inTheRange" and ftype == "date":
            self.out("[dim]Dates must be in YYYY-MM-DD format.[/dim]")
            return [
                self.prompt("From date", default="2020-01-01"),
                self.prompt("To date",   default="2025-12-31"),
            ]

        if ftype == "date":
            self.out("[dim]Format: YYYY-MM-DD  (e.g. 2024-06-15)[/dim]")
            return self.prompt("Date")

        if ftype == "number":
            hints = {
                "year":        "e.g. 1990",
                "rating":      "0 to 5",
                "playcount":   "e.g. 10",
                "bitrate":     "e.g. 320 for MP3, 900+ for lossless",
                "duration":    "in seconds  (e.g. 180 = 3 min)",
                "bpm":         "e.g. 120",
                "track":       "e.g. 1",
                "discnumber":  "e.g. 1",
                "size":        "in bytes  (e.g. 10000000 ~ 10 MB)",
                "channels":    "e.g. 2 for stereo",
                "bitdepth":    "e.g. 16, 24, 32",
            }
            if field in hints:
                self.out(f"[dim]{hints[field]}[/dim]")
            while True:
                raw = self.prompt(f"Value for \"{label}\"")
                try:
                    return self._parse_number(raw)
                except ValueError:
                    self.out("[red]Please enter a number.[/red]")

        # String
        examples = {
            "filetype":       "e.g. flac · mp3 · aac · ogg",
            "artist":         "e.g. Geto Boys",
            "albumartist":    "e.g. Geto Boys",
            "genre":          "e.g. Hip-Hop",
            "filepath":       "relative to music folder,  e.g. G/Geto Boys",
            "language":       "e.g. eng, fra, deu",
            "key":            "e.g. Cmaj, Amin",
            "releasetype":    "e.g. album, single, ep, compilation",
            "releasestatus":  "e.g. official, promotional, bootleg",
            "releasecountry": "e.g. US, GB, DE",
            "explicitstatus": "e.g. explicit, clean",
        }
        if field in examples:
            self.out(f"[dim]{examples[field]}[/dim]")
        return self.prompt(f"Value for \"{label}\"")

    def _show_conditions_summary(self, conditions: List[Dict], logic: str) -> None:
        if not conditions:
            return
        logic_label = "ALL must match" if logic == "all" else "ANY can match"
        lines = "\n".join(f"  {i}. {json.dumps(c)}" for i, c in enumerate(conditions, 1))
        self.panel(f"Logic: [bold]{logic_label}[/bold]\n\n{lines}", title="Rules so far")

    # ── Playlist wizard ───────────────────────────────────────────────────────

    def create_smart_playlist(self) -> Optional[Dict[str, Any]]:
        playlist: Dict[str, Any] = {}

        # ── Logic (ALL / ANY)
        self.rule("Rule Logic")
        self.out(
            "\n[dim]When you have multiple rules, should [bold]ALL[/bold] of them match,\n"
            "or is it enough for just [bold]ANY ONE[/bold] to match?[/dim]"
        )
        logic: str = self.select_option(
            "Combine rules with:",
            [
                ("all", "[bold]ALL[/bold] must match   [dim](AND - more selective)[/dim]"),
                ("any", "[bold]ANY[/bold] can match    [dim](OR  - more inclusive)[/dim]"),
            ],
        )  # type: ignore
        logic = str(logic)

        # ── Conditions
        self.rule("Build Rules")
        self.out(
            "\n[dim]Rules decide which tracks are included. You need at least one.\n"
            "Choose a category to add a rule, or select 'Nested rule group' for sub-AND/OR logic.[/dim]\n"
        )
        conditions: List[Dict[str, Any]] = []

        while True:
            condition = self.build_condition()
            if condition:
                conditions.append(condition)
                self._show_conditions_summary(conditions, logic)
                if not self.confirm("\nAdd another rule?", default=False):
                    break
            elif not conditions:
                # No rules yet and user cancelled — offer escape
                if not self.confirm("No rules added yet. Keep building this playlist?", default=True):
                    return None
            # else: cancelled while having rules — silently loop back

        playlist[logic] = conditions

        # ── Sorting
        self.rule("Sort Order")
        self.out("\n[dim]How should tracks be ordered in the playlist?[/dim]")

        sort_parts: List[str] = []
        while True:
            sort_key = self.select_option("Sort by:", self.sort_options)
            sort_key = str(sort_key)

            if sort_key == "random":
                sort_parts = ["random"]
                break

            direction = self.select_option(
                f"Direction for \"{sort_key}\":",
                [
                    ("asc",  "Ascending   [dim](oldest / lowest first)[/dim]"),
                    ("desc", "Descending  [dim](newest / highest first)[/dim]"),
                ],
            )
            direction = str(direction)
            prefix_char = "-" if direction == "desc" else "+"
            sort_parts.append(f"{prefix_char}{sort_key}")

            if not self.confirm("Add another sort field?", default=False):
                break

        if len(sort_parts) == 1:
            if sort_parts[0] == "random":
                playlist["sort"] = "random"
            else:
                field = sort_parts[0].lstrip("+-")
                is_desc = sort_parts[0].startswith("-")
                playlist["sort"] = field
                playlist["order"] = "desc" if is_desc else "asc"
        else:
            playlist["sort"] = ",".join(sort_parts)

        # ── Limit
        self.rule("Track Limit")
        if self.confirm("Limit the number of tracks in this playlist?", default=True):
            self.out("\n[dim]e.g. 50, 100, 500[/dim]")
            while True:
                raw = self.prompt("Max tracks", default="100")
                try:
                    playlist["limit"] = int(raw)
                    break
                except ValueError:
                    self.out("[red]Please enter a whole number.[/red]")

        # ── Name & description (at the end so you know what the playlist does)
        self.rule("Playlist Details")
        self.out("\n[dim]Now that you've built your rules, give the playlist a name.[/dim]")
        name = self.prompt("Name", default="My Smart Playlist")
        if name:
            playlist["name"] = name

        self.out("\n[dim]Optional: a short description (press Enter to skip).[/dim]")
        comment = self.prompt("Description", default="")
        if comment:
            playlist["comment"] = comment

        return playlist

    # ── Save ──────────────────────────────────────────────────────────────────

    def preview_and_save(self, playlist: Dict[str, Any]) -> None:
        self.rule("Preview")
        self.panel(json.dumps(playlist, indent=2), title="Generated Playlist JSON")

        if not self.confirm("\nSave this playlist?", default=True):
            self.out("[yellow]Discarded — nothing was saved.[/yellow]")
            return

        if not self.playlist_dir:
            self.out("[red]No save directory configured. Please set one first.[/red]")
            return

        default_name = "".join(
            c for c in playlist.get("name", "playlist").lower().replace(" ", "-")
            if c.isalnum() or c in "-_"
        ) or "playlist"
        self.out("\n[dim]Choose a filename (the .nsp extension will be added automatically).[/dim]")
        filename = self.prompt("Filename", default=default_name)
        if not filename.endswith(".nsp"):
            filename += ".nsp"

        filepath = self.playlist_dir / filename
        if filepath.exists():
            if not self.confirm(f"[yellow]{filename}[/yellow] already exists. Overwrite?", default=False):
                self.out("[yellow]Save cancelled.[/yellow]")
                return

        try:
            with open(filepath, "w") as f:
                json.dump(playlist, f, indent=2)
            self.out(f"\n[bold green]Saved to:[/bold green] {filepath}")
        except Exception as e:
            self.out(f"[red]Could not save: {e}[/red]")

    # ── Examples ─────────────────────────────────────────────────────────────

    def show_examples(self) -> None:
        examples = [
            ("Recently Played", {
                "name": "Recently Played",
                "comment": "Tracks played in the last 30 days",
                "all": [{"inTheLast": {"lastplayed": 30}}],
                "sort": "lastplayed", "order": "desc", "limit": 100,
            }),
            ("80s Favorites (nested logic)", {
                "name": "80s Favorites",
                "comment": "Loved or highly-rated songs from the 1980s",
                "all": [
                    {"any": [{"is": {"loved": True}}, {"gt": {"rating": 3}}]},
                    {"inTheRange": {"year": [1980, 1989]}},
                ],
                "sort": "year", "order": "desc", "limit": 50,
            }),
            ("High Quality (FLAC)", {
                "name": "High Quality",
                "comment": "Lossless tracks only",
                "all": [{"gt": {"bitrate": 900}}, {"is": {"filetype": "flac"}}],
                "sort": "random", "limit": 200,
            }),
            ("Loved Tracks", {
                "name": "Loved",
                "all": [{"is": {"loved": True}}],
                "sort": "dateloved", "order": "desc", "limit": 500,
            }),
            ("Never Played", {
                "name": "Never Played",
                "comment": "Tracks you haven't played yet",
                "all": [{"is": {"playcount": 0}}],
                "sort": "random", "limit": 200,
            }),
            ("Multi-sort Example", {
                "name": "By Artist then Year",
                "comment": "Sorted by artist ascending, then year descending",
                "all": [{"gt": {"playcount": -1}}],
                "sort": "+artist,-year",
            }),
        ]
        self.rule("Example Playlists")
        for title, data in examples:
            self.out(f"\n[bold yellow]{title}[/bold yellow]")
            self.out(json.dumps(data, indent=2))
        self.out()

    def show_all_fields(self) -> None:
        self.rule("Available Fields")
        if RICH_AVAILABLE and self.console:
            for category, entries in self.fields.items():
                t = Table(title=category, show_header=True, header_style="bold magenta", box=None)
                t.add_column("Field",       style="cyan", width=30)
                t.add_column("Description", style="white")
                t.add_column("Type",        style="dim",  width=10)
                for key, desc, ftype in entries:
                    t.add_row(key, desc, ftype)
                self.console.print(t)
                self.console.print()
        else:
            for category, entries in self.fields.items():
                print(f"\n{category}:")
                for key, desc, ftype in entries:
                    print(f"  {key:<30} {desc} ({ftype})")

    # ── Presets ─────────────────────────────────────────────────────────────

    PRESETS: List[Tuple[str, str, str, Dict[str, Any]]] = [
        # (menu_label, filename, category, playlist_dict)

        # ── Essentials ─────────────────────────────────────────────────
        ("Recently Played", "recently-played", "Essentials", {
            "name": "Recently Played",
            "comment": "Tracks played in the last 30 days",
            "all": [{"inTheLast": {"lastplayed": 30}}],
            "sort": "lastplayed", "order": "desc", "limit": 100,
        }),
        ("Recently Added", "recently-added", "Essentials", {
            "name": "Recently Added",
            "comment": "Tracks added to the library in the last 30 days",
            "all": [{"inTheLast": {"dateadded": 30}}],
            "sort": "dateadded", "order": "desc", "limit": 200,
        }),
        ("Most Played", "most-played", "Essentials", {
            "name": "Most Played",
            "comment": "Your top 100 most-played tracks of all time",
            "all": [{"gt": {"playcount": 0}}],
            "sort": "playcount", "order": "desc", "limit": 100,
        }),
        ("Never Played", "never-played", "Essentials", {
            "name": "Never Played",
            "comment": "Tracks you haven't listened to yet",
            "all": [{"is": {"playcount": 0}}],
            "sort": "random", "limit": 200,
        }),
        ("Loved Tracks", "loved-tracks", "Essentials", {
            "name": "Loved Tracks",
            "comment": "All your favourited tracks, newest first",
            "all": [{"is": {"loved": True}}],
            "sort": "dateloved", "order": "desc", "limit": 500,
        }),
        ("Top Rated", "top-rated", "Essentials", {
            "name": "Top Rated",
            "comment": "Tracks rated 4 stars or higher",
            "all": [{"gt": {"rating": 3}}],
            "sort": "rating", "order": "desc", "limit": 200,
        }),

        # ── Discovery ──────────────────────────────────────────────────
        ("Fresh Blood", "fresh-blood", "Discovery", {
            "name": "Fresh Blood",
            "comment": "Added in the last 7 days and never played — your unheard new arrivals",
            "all": [
                {"inTheLast": {"dateadded": 7}},
                {"is": {"playcount": 0}},
            ],
            "sort": "random", "limit": 100,
        }),
        ("Vinyl Roulette", "vinyl-roulette", "Discovery", {
            "name": "Vinyl Roulette",
            "comment": "50 completely random tracks — spin the wheel",
            "all": [{"gt": {"duration": 0}}],
            "sort": "random", "limit": 50,
        }),
        ("One-Hit Wonders", "one-hit-wonders", "Discovery", {
            "name": "One-Hit Wonders",
            "comment": "Tracks you've played exactly once — give them a second chance",
            "all": [{"is": {"playcount": 1}}],
            "sort": "random", "limit": 100,
        }),
        ("Album Openers", "album-openers", "Discovery", {
            "name": "Album Openers",
            "comment": "Track 1 from every album — first impressions only",
            "all": [{"is": {"track": 1}}],
            "sort": "random", "limit": 100,
        }),

        # ── Rediscovery ────────────────────────────────────────────────
        ("Forgotten Gems", "forgotten-gems", "Rediscovery", {
            "name": "Forgotten Gems",
            "comment": "Loved or highly-rated tracks you haven't played in 6+ months",
            "all": [
                {"any": [{"is": {"loved": True}}, {"gt": {"rating": 3}}]},
                {"notInTheLast": {"lastplayed": 180}},
            ],
            "sort": "random", "limit": 100,
        }),
        ("Comebacks", "comebacks", "Rediscovery", {
            "name": "Comebacks",
            "comment": "Played 5+ times but not in the last 6 months — old favourites gathering dust",
            "all": [
                {"gt": {"playcount": 4}},
                {"notInTheLast": {"lastplayed": 180}},
            ],
            "sort": "random", "limit": 100,
        }),
        ("Buried Treasure", "buried-treasure", "Rediscovery", {
            "name": "Buried Treasure",
            "comment": "Added over a year ago and never played — lost in the stacks",
            "all": [
                {"notInTheLast": {"dateadded": 365}},
                {"is": {"playcount": 0}},
            ],
            "sort": "random", "limit": 100,
        }),

        # ── Moods & Vibes ──────────────────────────────────────────────
        ("Long Drives", "long-drives", "Moods & Vibes", {
            "name": "Long Drives",
            "comment": "Epic tracks over 6 minutes — settle in for the ride",
            "all": [{"gt": {"duration": 360}}],
            "sort": "duration", "order": "desc", "limit": 100,
        }),
        ("Short & Sweet", "short-and-sweet", "Moods & Vibes", {
            "name": "Short & Sweet",
            "comment": "Quick hits under 3 minutes",
            "all": [{"lt": {"duration": 180}}],
            "sort": "random", "limit": 100,
        }),
        ("Deep Cuts", "deep-cuts", "Moods & Vibes", {
            "name": "Deep Cuts",
            "comment": "Tracks 5+ on the album — beyond the singles",
            "all": [{"gt": {"track": 4}}],
            "sort": "random", "limit": 100,
        }),
        ("Slow Burners", "slow-burners", "Moods & Vibes", {
            "name": "Slow Burners",
            "comment": "Tracks under 100 BPM — chill, downtempo, mellow",
            "all": [
                {"lt": {"bpm": 100}},
                {"gt": {"bpm": 0}},
            ],
            "sort": "bpm", "order": "asc", "limit": 100,
        }),
        ("Bangers Only", "bangers-only", "Moods & Vibes", {
            "name": "Bangers Only",
            "comment": "High-energy tracks over 140 BPM",
            "all": [{"gt": {"bpm": 140}}],
            "sort": "bpm", "order": "desc", "limit": 100,
        }),

        # ── Quality & Format ──────────────────────────────────────────
        ("FLAC Attack", "flac-attack", "Quality & Format", {
            "name": "FLAC Attack",
            "comment": "Lossless FLAC files only — audiophile approved",
            "all": [{"is": {"filetype": "flac"}}],
            "sort": "random", "limit": 200,
        }),
        ("Hi-Res Audio", "hi-res-audio", "Quality & Format", {
            "name": "Hi-Res Audio",
            "comment": "24-bit or higher — studio master quality",
            "all": [{"gt": {"bitdepth": 16}}],
            "sort": "random", "limit": 200,
        }),
        ("Lossy Leftovers", "lossy-leftovers", "Quality & Format", {
            "name": "Lossy Leftovers",
            "comment": "Tracks under 320kbps — candidates for upgrade",
            "all": [{"lt": {"bitrate": 320}}],
            "sort": "+artist,+album,+track",
        }),

        # ── Decades ───────────────────────────────────────────────────
        ("60s Classics", "60s-classics", "Decades", {
            "name": "60s Classics",
            "comment": "Everything from 1960–1969",
            "all": [{"inTheRange": {"year": [1960, 1969]}}],
            "sort": "random", "limit": 200,
        }),
        ("70s Classics", "70s-classics", "Decades", {
            "name": "70s Classics",
            "comment": "Everything from 1970–1979",
            "all": [{"inTheRange": {"year": [1970, 1979]}}],
            "sort": "random", "limit": 200,
        }),
        ("80s Classics", "80s-classics", "Decades", {
            "name": "80s Classics",
            "comment": "Everything from 1980–1989",
            "all": [{"inTheRange": {"year": [1980, 1989]}}],
            "sort": "random", "limit": 200,
        }),
        ("90s Classics", "90s-classics", "Decades", {
            "name": "90s Classics",
            "comment": "Everything from 1990–1999",
            "all": [{"inTheRange": {"year": [1990, 1999]}}],
            "sort": "random", "limit": 200,
        }),
        ("2000s Classics", "2000s-classics", "Decades", {
            "name": "2000s Classics",
            "comment": "Everything from 2000–2009",
            "all": [{"inTheRange": {"year": [2000, 2009]}}],
            "sort": "random", "limit": 200,
        }),
        ("2010s Classics", "2010s-classics", "Decades", {
            "name": "2010s Classics",
            "comment": "Everything from 2010–2019",
            "all": [{"inTheRange": {"year": [2010, 2019]}}],
            "sort": "random", "limit": 200,
        }),

        # ── Complex / Nested ──────────────────────────────────────────
        ("80s Gold", "80s-gold", "Complex / Nested", {
            "name": "80s Gold",
            "comment": "Loved or highly-rated tracks from the 1980s (nested logic)",
            "all": [
                {"any": [{"is": {"loved": True}}, {"gt": {"rating": 3}}]},
                {"inTheRange": {"year": [1980, 1989]}},
            ],
            "sort": "year", "order": "desc", "limit": 50,
        }),
        ("The Collector", "the-collector", "Complex / Nested", {
            "name": "The Collector",
            "comment": "Played 10+ times AND (loved OR rated 4+) — your true obsessions",
            "all": [
                {"gt": {"playcount": 9}},
                {"any": [{"is": {"loved": True}}, {"gt": {"rating": 3}}]},
            ],
            "sort": "playcount", "order": "desc",
        }),
        ("Guilty Pleasures", "guilty-pleasures", "Complex / Nested", {
            "name": "Guilty Pleasures",
            "comment": "High play count but never loved or rated — your secret shames",
            "all": [
                {"gt": {"playcount": 5}},
                {"isNot": {"loved": True}},
                {"is": {"rating": 0}},
            ],
            "sort": "playcount", "order": "desc", "limit": 100,
        }),
        ("Compilation Cuts", "compilation-cuts", "Complex / Nested", {
            "name": "Compilation Cuts",
            "comment": "Tracks from compilation albums you've loved or played often",
            "all": [
                {"is": {"compilation": True}},
                {"any": [{"is": {"loved": True}}, {"gt": {"playcount": 3}}]},
            ],
            "sort": "random", "limit": 100,
        }),
        ("Peak Album Experience", "peak-album-experience", "Complex / Nested", {
            "name": "Peak Album Experience",
            "comment": "Loved tracks from their original disc 1, ordered by album then track",
            "all": [
                {"is": {"loved": True}},
                {"is": {"discnumber": 1}},
            ],
            "sort": "+albumartist,+album,+track",
        }),
        ("The Graveyard", "the-graveyard", "Complex / Nested", {
            "name": "The Graveyard",
            "comment": "Tracks added over 2 years ago, played once or never, and not loved — do they deserve to stay?",
            "all": [
                {"notInTheLast": {"dateadded": 730}},
                {"lt": {"playcount": 2}},
                {"isNot": {"loved": True}},
            ],
            "sort": "dateadded", "order": "asc", "limit": 200,
        }),
    ]

    def deploy_presets(self) -> None:
        """Let the user pick presets to deploy as .nsp files."""
        self.rule("Presets")
        self.out(
            "\n[dim]Ready-made smart playlists you can deploy instantly.\n"
            "Pick one to preview and save, or deploy them all at once.[/dim]\n"
        )

        # Build menu grouped by category
        categories: Dict[str, List[int]] = {}
        for i, (_, _, cat, _) in enumerate(self.PRESETS):
            categories.setdefault(cat, []).append(i)

        options: List[Tuple[Any, str]] = [
            ("__all__", "[bold green]Deploy ALL presets at once[/bold green]")
        ]
        for cat, indices in categories.items():
            for idx in indices:
                label, _, _, preset = self.PRESETS[idx]
                options.append((idx, f"[dim][{cat}][/dim]  {label}"))

        while True:
            choice = self.select_option("Choose a preset:", options, allow_back=True)
            if choice is None:
                return

            if choice == "__all__":
                self._deploy_all_presets()
                return

            idx = int(str(choice))
            label, filename, cat, preset = self.PRESETS[idx]
            self.out(f"\n[bold yellow]{label}[/bold yellow]  [dim]({cat})[/dim]")
            self.out(json.dumps(preset, indent=2))
            if self.confirm(f"\nSave as [cyan]{filename}.nsp[/cyan]?", default=True):
                self._save_preset(filename, preset)

    def _deploy_all_presets(self) -> None:
        """Deploy every preset at once."""
        saved = 0
        skipped = 0
        for label, filename, _, preset in self.PRESETS:
            filepath = self.playlist_dir / f"{filename}.nsp"  # type: ignore
            if filepath.exists():
                self.out(f"  [yellow]Skipped:[/yellow] {filename}.nsp (already exists)")
                skipped += 1
            else:
                try:
                    with open(filepath, "w") as f:
                        json.dump(preset, f, indent=2)
                    self.out(f"  [green]Saved:[/green] {filename}.nsp")
                    saved += 1
                except Exception as e:
                    self.out(f"  [red]Error:[/red] {filename}.nsp — {e}")
        self.out(f"\n[bold green]Done:[/bold green] {saved} saved, {skipped} skipped")

    def _save_preset(self, filename: str, preset: Dict[str, Any]) -> None:
        """Save a single preset."""
        if not self.playlist_dir:
            self.out("[red]No save directory configured.[/red]")
            return
        filepath = self.playlist_dir / f"{filename}.nsp"
        if filepath.exists():
            if not self.confirm(f"[yellow]{filename}.nsp[/yellow] already exists. Overwrite?", default=False):
                self.out("[yellow]Skipped.[/yellow]")
                return
        try:
            with open(filepath, "w") as f:
                json.dump(preset, f, indent=2)
            self.out(f"[bold green]Saved to:[/bold green] {filepath}")
        except Exception as e:
            self.out(f"[red]Could not save: {e}[/red]")

    # ── Main menu ─────────────────────────────────────────────────────────────

    def main_menu(self) -> None:
        while True:
            self.out()
            self.banner()
            self.out()
            if self.playlist_dir:
                self.out(f"[green]Save directory:[/green] {self.playlist_dir}")
            else:
                self.out("[bold red]  No save directory set — configure one before creating playlists.[/bold red]")
            self.out()

            choice = self.select_option(
                "What would you like to do?",
                [
                    ("create",    "Create a new smart playlist"),
                    ("presets",   "Deploy preset playlists"),
                    ("examples",  "Browse example JSON"),
                    ("fields",    "View all available fields"),
                    ("directory", "Set / change save directory"),
                    ("exit",      "Exit"),
                ],
            )

            if choice == "create":
                if not self.playlist_dir:
                    self.out("[yellow]Please set a save directory first.[/yellow]")
                    self.set_playlist_directory()
                    if not self.playlist_dir:
                        continue
                playlist = self.create_smart_playlist()
                if playlist:
                    self.preview_and_save(playlist)

            elif choice == "presets":
                if not self.playlist_dir:
                    self.out("[yellow]Please set a save directory first.[/yellow]")
                    self.set_playlist_directory()
                    if not self.playlist_dir:
                        continue
                self.deploy_presets()

            elif choice == "examples":
                self.show_examples()

            elif choice == "fields":
                self.show_all_fields()

            elif choice == "directory":
                self.set_playlist_directory()

            elif choice == "exit":
                self.out("\n[cyan]Goodbye![/cyan]")
                break


def main() -> None:
    try:
        SmartPlaylistCreator().main_menu()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
