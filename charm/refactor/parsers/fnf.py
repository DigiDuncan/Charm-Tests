from __future__ import annotations

import json
import logging
import math
from pathlib import Path
from typing import TypedDict

from charm.lib.errors import ChartPostReadParseError, UnknownLanesError
from charm.lib.types import Milliseconds
from charm.objects.lyric_animator import LyricEvent
from charm.refactor.charts.fnf import CameraFocusEvent, FNFChart, FNFNote, FNFNoteType
from charm.refactor.generic.chart import BPMChangeEvent, Event, ChartMetadata
from charm.refactor.generic.parser import Parser

logger = logging.getLogger("charm")

class NoteJson(TypedDict):
    bpm: float
    mustHitSection: bool
    sectionNotes: list[tuple[Milliseconds, int, Milliseconds]]
    lengthInSteps: int

class SongJson(TypedDict):
    song: str
    bpm: float
    speed: float
    notes: list[NoteJson]

class SongFileJson(TypedDict):
    song: SongJson

class FNFParser(Parser[FNFChart]):
    @staticmethod
    def parse_metadata(path: Path) -> list[ChartMetadata]:
        stem = path.stem
        charts = path.glob(f"./{stem}*.json")
        return [ChartMetadata('fnf', chart_path.stem.casefold().removeprefix(f'{stem.casefold()}').removeprefix('-') or 'normal', chart_path, '1') for chart_path in charts]

    @staticmethod
    def parse_chart(chart_data: ChartMetadata) -> list[FNFChart]:
        with open(chart_data.path) as p:
            j: SongFileJson = json.load(p)
        fnf_overrides = None
        override_path = chart_data.path.parent / "fnf.json"
        if override_path.exists() and override_path.is_file():
            with open(override_path) as f:
                fnf_overrides = json.load(f)
        songdata = j["song"]

        name = songdata["song"].replace("-", " ").title()
        logger.debug(f"Parsing {name}...")
        bpm = songdata["bpm"]
        speed = songdata["speed"]  # !: Speed used to be on the FNFChart, but FNFChart is dead!

        p1_metadata = ChartMetadata(chart_data.gamemode, chart_data.difficulty, chart_data.path, "1")
        p2_metadata = ChartMetadata(chart_data.gamemode, chart_data.difficulty, chart_data.path, "2")
        charts = [
            FNFChart(p1_metadata, [], [], bpm),
            FNFChart(p2_metadata, [], [], bpm)
        ]

        for chart in charts:
            chart.bpm = bpm

        song_sections = songdata["song"]  # noqa: F841 -- currently unused, what's in here?

        last_bpm = bpm
        last_focus: int | None = None
        section_start = 0.0
        events: list[Event] = []
        sections = songdata["notes"]
        section_starts = []
        unknown_lanes = []

        for section in sections:
            # There's a changeBPM event but like, it always has to be paired
            # with a bpm, so it's pointless anyway
            if "bpm" in section:
                new_bpm = section["bpm"]
                if new_bpm != last_bpm:
                    events.append(BPMChangeEvent(section_start, new_bpm))
                    last_bpm = new_bpm
            section_starts.append((section_start, bpm))

            # Since in theory you can have events in these sections
            # without there being notes there, I need to calculate where this
            # section occurs from scratch, and some engines have a startTime
            # thing here but I can't guarantee it so it's basically pointless
            seconds_per_beat = 60 / bpm
            seconds_per_measure = seconds_per_beat * 4
            seconds_per_sixteenth = seconds_per_measure / 16
            if "lengthInSteps" in section:
                section_length = section["lengthInSteps"] * seconds_per_sixteenth
            elif "sectionBeats" in section:
                section_length = section["sectionBeats"] * seconds_per_sixteenth * 4  # Psych Engine recommends this now! yay /s
            else:
                raise ChartPostReadParseError("Notes section missing length!")

            # Create a camera focus event like they should have in the first place
            # mustHitSection indicates the "active player" is the real player (P1).
            # All this really controls is the camera, (because despite the name you have
            # to hit all the notes in all sections), but has the side effect of flipping
            # what lane corrosponds to what player. I fix this by treating the chart's
            # "player 0" to mean "the focused player".
            if section["mustHitSection"]:
                focused, unfocused = 0, 1
            else:
                focused, unfocused = 1, 0

            if focused != last_focus:
                events.append(CameraFocusEvent(section_start, focused))
                last_focus = focused

            # Lanemap: (player, lane, type)
            if fnf_overrides:
                # This is done because some mods use "extra lanes" differents, so I have to provide
                # a file that maps them to the right lane.
                lanemap = [(lane[0], lane[1], getattr(FNFNoteType, lane[2])) for lane in fnf_overrides["lanes"]]
            else:
                lanemap: list[tuple[int, int, FNFNoteType]] = [(0, 0, FNFNoteType.NORMAL), (0, 1, FNFNoteType.NORMAL), (0, 2, FNFNoteType.NORMAL), (0, 3, FNFNoteType.NORMAL),
                                                               (1, 0, FNFNoteType.NORMAL), (1, 1, FNFNoteType.NORMAL), (1, 2, FNFNoteType.NORMAL), (1, 3, FNFNoteType.NORMAL)]
            # Actually make two charts
            section_notes = section["sectionNotes"]
            for note in section_notes:
                extra = None
                if len(note) > 3:
                    extra = note[3:]
                    note = note[:3]
                posms, lane, lengthms = note  # hope this never breaks lol
                # EDIT: It does break, sometimes!
                if lane < 0:
                    continue  # I don't know what to do with these yet.
                pos = posms / 1000
                length = lengthms / 1000

                try:
                    note_data = lanemap[lane]
                except IndexError:
                    unknown_lanes.append(lane)
                    continue

                if note_data[0] == 0:
                    note_player = focused
                elif note_data[0] == 1:
                    note_player = unfocused
                else:
                    note_player = note_data[0]  # If the note_player isn't 0/1, this is going to break, realistically, but we want to know that.
                chart_lane = note_data[1]
                note_type = note_data[2]

                thisnote = FNFNote(charts[note_player], pos, chart_lane, length, type = note_type)
                thisnote.extra_data = extra  # Append that data we don't know what to do with, in case one day we do
                if thisnote.type in [FNFNoteType.BOMB, FNFNoteType.DEATH, FNFNoteType.HEAL, FNFNoteType.CAUTION]:
                    thisnote.length = 0  # why do these ever have length?
                if thisnote.length < 0.001:
                    thisnote.length = 0
                charts[note_player].notes.append(thisnote)

                # TODO: Fake sustains (change this?)
                # We basically generate an invisible "sustain" note every 16th-beat. The original game does it
                # but I wish we were doing something better than this, like just doing sustain calculation in-engine
                # while a sustain is active.
                if thisnote.length != 0:
                    sustainbeats = round(thisnote.length / seconds_per_sixteenth)
                    for i in range(sustainbeats):
                        thatnote = FNFNote(charts[note_player], pos + (seconds_per_sixteenth * (i + 1)), chart_lane, 0, FNFNoteType.SUSTAIN)
                        thatnote.parent = thisnote
                        charts[note_player].notes.append(thatnote)

            section_start += section_length

        # LYRICS
        lyrics = []

        # Pysch Engine events look like this
        if "events" in songdata:
            events = songdata["events"]
            for e in events:  # * HEY DRAGON CHECK THIS OUT
                time = e[0] / 1000
                subevents = e[1]
                for s in subevents:
                    t, d1, d2 = s
                    if t == "lyrics":
                        lyrics.append(LyricEvent(time, None, d1))  # type: ignore None is a stop-gap for a later stage of parsing

            # Psych Engine lyrics
            if lyrics:
                lyrics[-1].length = math.inf
                for n, lyric_event in enumerate(lyrics[:-1]):
                    lyric_event.length = lyrics[n + 1].time - lyric_event.time

            for c in charts:
                c.events.extend(lyrics)

        for c in charts:
            c.events = events
            c.notes.sort()
            c.events.sort()
            logger.debug(f"Parsed chart {c.metadata.instrument} with {len(c.notes)} notes.")

        unknown_lanes = sorted(set(unknown_lanes))
        if unknown_lanes:
            raise UnknownLanesError(f"Unknown lanes found in chart {name}: {unknown_lanes}")

        return charts