from typing import List, Tuple

NEIGHBOR_OFFSETS = [
    (dx, dy)
    for dx in (-1, 0, 1)
    for dy in (-1, 0, 1)
    if not (dx == 0 and dy == 0)
]

def get_neighbors(x, y, w, h) -> List[Tuple[int, int]]:
    neighbors = []
    for dx, dy in NEIGHBOR_OFFSETS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h:
            neighbors.append((nx, ny))
    return neighbors

with open("input.txt") as f:
    grid = [list(line.strip()) for line in f if line.strip()]

h = len(grid)
w = len(grid[0]) if h else 0
count_accessible_1, count_accessible_2 = 0, 0

for y in range(h):
    for x in range(w):
        if grid[y][x] == '@':
            neighbors = get_neighbors(x, y, w, h)
            if sum(1 for nx, ny in neighbors if grid[ny][nx] == '@') < 4:
                count_accessible_1 += 1
rm_rolls = True
while rm_rolls:
    rm_rolls = False
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '@':
                neighbors = get_neighbors(x, y, w, h)
                if sum(1 for nx, ny in neighbors if grid[ny][nx] == '@') < 4:
                    count_accessible_2 += 1
                    grid[y][x] = '.'
                    rm_rolls = True

print(f"[Part 1]: {count_accessible_1}")
print(f"[Part 2]: {count_accessible_2}")