"""Standardized input parsing for Advent of Code solutions."""

import re
from pathlib import Path


def _resolve(path: str) -> Path:
    return Path(path)


def read_raw(path: str) -> str:
    """Entire file as a single string (trailing newline stripped)."""
    return _resolve(path).read_text().strip()


def read_lines(path: str) -> list[str]:
    """File split into lines, each stripped of trailing whitespace."""
    return read_raw(path).split("\n")


def read_grid(path: str) -> list[list[str]]:
    """File as a 2D character grid (list of lists)."""
    return [list(line) for line in read_lines(path)]


def read_ints(path: str) -> list[int]:
    """One integer per line."""
    return [int(line) for line in read_lines(path)]


def read_groups(path: str) -> list[list[str]]:
    """Sections separated by blank lines, each section a list of lines."""
    raw = read_raw(path)
    return [group.split("\n") for group in raw.split("\n\n")]


def read_csv(path: str, sep: str = ",") -> list[str]:
    """Single-line file split by a delimiter (default comma)."""
    return read_raw(path).split(sep)


def ints(text: str) -> list[int]:
    """Extract all integers (including negative) from a string.

    >>> ints("pos=<-3, 14>, vel=<2, -7>")
    [-3, 14, 2, -7]
    """
    return list(map(int, re.findall(r"-?\d+", text)))
