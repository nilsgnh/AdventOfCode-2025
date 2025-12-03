def get_highest_digit(line: str, min_space: int):
    end = len(line) - min_space
    pos, char = max(
        enumerate(line[:end]),
        key=lambda t: t[1]
    )
    return int(char), pos

def build_number(line: str, char_range):
    digits = []
    offset = 0
    for msa in char_range:
        digit, pos = get_highest_digit(line[offset:], msa)
        digits.append(str(digit))
        offset += pos + 1
    return int("".join(digits))

with open("input.txt") as f:
    lines = [l.strip() for l in f if l.strip()]

sum1 = sum(build_number(line, [1, 0]) for line in lines)
sum2 = sum(build_number(line, range(11, -1, -1)) for line in lines)

print(f"[Part 1]: {sum1}")
print(f"[Part 2]: {sum2}")