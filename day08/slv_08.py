import math
from collections import defaultdict
from itertools import combinations

def straight_line_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

def find_root(x):
    if rootList[x] != x:
        rootList[x] = find_root(rootList[x])
    return rootList[x]

def union(x, y):
    rootX = find_root(x)
    rootY = find_root(y)
    if rootX != rootY:
        rootList[rootY] = rootX
        return True
    return False

with open('input.txt') as f:
    points = [tuple(map(int, line.strip().split(','))) for line in f]

n = len(points)
rootList = list(range(n))

distances = []
for (i, p1), (j, p2) in combinations(enumerate(points), 2):
    dist = straight_line_distance(p1, p2)
    distances.append((dist, i, j))
distances.sort()

pairs_seen = 0
unions_done = 0
part1_result = None
part2_result = None
for _, i, j in distances:
    pairs_seen += 1

    if union(i, j):
        unions_done += 1
        if unions_done == n - 1 and part2_result is None:
            part2_result = points[i][0] * points[j][0]

    if pairs_seen == 1000 and part1_result is None:
        comp_size = defaultdict(int)
        for i in range(n):
            comp_size[find_root(i)] += 1
        sizes =  sorted(comp_size.values(), reverse=True)
        part1_result = sizes[0] * sizes[1] * sizes[2]

print("Part 1:", part1_result)
print("Part 2:", part2_result)