import datetime

start_time = datetime.datetime.now()

with open('input.txt', 'r') as file:
    data = [line.strip().split() for line in file.readlines()]

moves = [(line[0][0], int(line[0][1:])) for line in data]

dialCount = 50
nullAtEndCounter = 0 # Part 1
nullPassingCounter = 0 # Part 2

for direction, distance in moves:
    if direction == "R":
        nullPassingCounter += (distance + dialCount) // 100
        dialCount = (dialCount + distance) % 100
    elif direction == "L":
        nullPassingCounter += (distance - dialCount) // 100 - ((-1)*dialCount // 100)
        dialCount = (dialCount - distance) % 100

    if dialCount == 0:
        nullAtEndCounter += 1
print(f"[Part 1]: Anzahl 0en auf Endposition: {nullAtEndCounter}")
print(f"[Part 2]: Anzahl 0en beim Durchlaufen: {nullPassingCounter}")

end_time = datetime.datetime.now()
print(f"Execution Time: {end_time - start_time}")
