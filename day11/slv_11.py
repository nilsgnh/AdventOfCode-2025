with open('input.txt') as f:
    devices = {}
    for line in f:
        parts = line.strip().split(': ')
        device = parts[0]
        outputs = parts[1].split(' ')
        devices[device] = outputs

def count_paths(devices, start, end):
    stack = [(start, [start])]
    path_count = 0

    while stack:
        (vertex, path) = stack.pop()
        for next_device in devices.get(vertex, []):
            if next_device == end:
                path_count += 1
            else:
                if next_device not in path:
                    stack.append((next_device, path + [next_device]))
    return path_count

def dfs(node, end, devices, seen_dac, seen_fft, memo):
    key = (node, seen_dac, seen_fft)

    if key in memo:
        return memo[key]

    if node == end:
        result = 1 if (seen_dac and seen_fft) else 0
        memo[key] = result
        return result

    total = 0
    for nextdev in devices.get(node, []):
        total += dfs(nextdev,end,devices,seen_dac or (nextdev == 'dac'),seen_fft or (nextdev == 'fft'),memo)

    memo[key] = total
    return total


def count_paths_2(devices, start, end):
    memo = {}
    return dfs(start, end, devices, start == 'dac', start == 'fft', memo)

total_paths = count_paths(devices, 'you', 'out')
print(f"Part 1: {total_paths}")

total_paths2 = count_paths_2(devices, 'svr', 'out')
print(f"Part 2: {total_paths2}")