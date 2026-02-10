"""Common grid and traversal utilities for Advent of Code."""

from collections import deque

# Direction constants
DIRS_4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
DIRS_8 = DIRS_4 + [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Named direction maps (useful for parsing movement instructions)
DIR_MAP = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
}


def in_bounds(r: int, c: int, rows: int, cols: int) -> bool:
    """Check if (r, c) is within grid bounds."""
    return 0 <= r < rows and 0 <= c < cols


def neighbors(
    r: int, c: int, rows: int, cols: int, dirs: list[tuple[int, int]] = DIRS_4
) -> list[tuple[int, int]]:
    """Return in-bounds neighbor coordinates."""
    return [
        (r + dr, c + dc) for dr, dc in dirs if in_bounds(r + dr, c + dc, rows, cols)
    ]


def find_char(grid: list[list[str]], ch: str) -> tuple[int, int] | None:
    """Find first occurrence of a character in a 2D grid."""
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == ch:
                return (r, c)
    return None


def find_all_char(grid: list[list[str]], ch: str) -> list[tuple[int, int]]:
    """Find all occurrences of a character in a 2D grid."""
    return [
        (r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == ch
    ]


def bfs(start: tuple[int, int], neighbors_fn) -> dict[tuple[int, int], int]:
    """Generic BFS from a start position.

    neighbors_fn(pos) should return an iterable of reachable neighbor positions.
    Returns a dict mapping each reachable position to its distance from start.
    """
    dist: dict[tuple[int, int], int] = {start: 0}
    queue = deque([start])
    while queue:
        pos = queue.popleft()
        for nxt in neighbors_fn(pos):
            if nxt not in dist:
                dist[nxt] = dist[pos] + 1
                queue.append(nxt)
    return dist


def print_grid(grid: list[list[str]]) -> None:
    """Pretty-print a 2D grid for debugging."""
    for row in grid:
        print("".join(row))
