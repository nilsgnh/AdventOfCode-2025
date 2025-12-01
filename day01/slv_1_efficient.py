with open('input.txt', 'r') as file:
    data = [line.strip().split() for line in file.readlines()]

moves = [(line[0][0], int(line[0][1:])) for line in data]

dialCount = 50
nullAtEndCounter = nullPassingCounter = 0

for direction, distance in moves:
    vz = -1 if direction == "L" else 1
    nullPassingCounter += (distance + vz * dialCount) // 100 - (vz*dialCount // 100)
    dialCount = (dialCount + vz* distance) % 100
    if dialCount == 0:
        nullAtEndCounter += 1
        
print(f"[Part 1]: {nullAtEndCounter}")
print(f"[Part 2]: {nullPassingCounter}")