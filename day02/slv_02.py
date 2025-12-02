def test_invalid_id_part1(test_id):
    strid = str(test_id)
    mid = len(strid) // 2
    return strid[:mid] == strid[mid:]

def test_invalid_id_part2(test_id):
    strid = str(test_id)
    n = len(strid)
    for i in range(1, n//2 + 1):
        if n % i == 0:
            part = strid[:i]
            if part * (n//i) == strid:
                return True
    return False

with open("input.txt") as f:
    ranges = [tuple(map(int, r.split("-"))) for r in f.read().strip().split(",")]

sum_invalid_ids_part1 = 0
sum_invalid_ids_part2 = 0

for start, end in ranges:
    for i in range(start, end + 1):
        if test_invalid_id_part1(i):
            sum_invalid_ids_part1 += i
        if test_invalid_id_part2(i):
            sum_invalid_ids_part2 += i

print(f"[Part 1]: {sum_invalid_ids_part1}")
print(f"[Part 2]: {sum_invalid_ids_part2}")