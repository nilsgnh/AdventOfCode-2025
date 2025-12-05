with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

intervalle = []
for i, line in enumerate(lines):
    if '-' not in line:
        break
    start, end = map(int, line.split('-'))
    intervalle.append((start, end))

ids = [int(lines[j]) for j in range(i, len(lines))]

count_freshids = 0
for id_ in ids:
    if any(start <= id_ <= end for start, end in intervalle):
        count_freshids += 1

print(f"[Part 1]: {count_freshids}")

intervalle_sorted = sorted(intervalle, key=lambda r: r[0])

distinct_intervals = []
for start, end in intervalle_sorted:
    if not distinct_intervals:
        distinct_intervals.append([start, end])
    else:
        last_start, last_end = distinct_intervals[-1]
        if start <= last_end + 1:
            distinct_intervals[-1][1] = max(last_end, end)
        else:
            distinct_intervals.append([start, end])

total_freshid_count = sum(end - start + 1 for start, end in distinct_intervals)
print(f"[Part 2]: {total_freshid_count}")