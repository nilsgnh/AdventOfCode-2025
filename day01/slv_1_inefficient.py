with open('input.txt', 'r') as file:
    data = [line.strip().split() for line in file.readlines()]

moves = [(line[0][0], int(line[0][1:])) for line in data]

dialCount = 50
nullAtEndCounter = nullPassingCounter = 0

for direction, distance in moves:
    step = -1 if direction == "L" else 1
    for _ in range(distance):
        dialCount = (dialCount + step) % 100
        nullPassingCounter += 1 if dialCount == 0 else 0
    if dialCount == 0:
        nullAtEndCounter += 1

print(f"[Part 1]: {nullAtEndCounter}")
print(f"[Part 2]: {nullPassingCounter}")