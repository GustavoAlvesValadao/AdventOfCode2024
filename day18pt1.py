from collections import deque

GRID_SIZE = 71

byte_positions = [
    (5, 4), (4, 2), (4, 5), (3, 0), (2, 1), (6, 3), (2, 4), (1, 5), (0, 6),
    (3, 3), (2, 6), (5, 1), (1, 2), (5, 5), (2, 5), (6, 5), (1, 4), (0, 4),
    (6, 4), (1, 1), (6, 1), (1, 0), (0, 5), (1, 6), (2, 0)
]

while len(byte_positions) < 1024:
    byte_positions.extend(byte_positions)

byte_positions = byte_positions[:1024]

byte_positions = [(x % GRID_SIZE, y % GRID_SIZE) for x, y in byte_positions]

grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for x, y in byte_positions:
    grid[y][x] = '#'

def bfs(grid, start, end):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
    queue = deque([(start[0], start[1], 0)]) 
    visited = set() 

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            return steps

        if (x, y) in visited or grid[y][x] == '#':
            continue

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE: 
                queue.append((nx, ny, steps + 1))

    return -1

start = (0, 0)
end = (70, 70)

min_steps = bfs(grid, start, end)

print(f"O número mínimo de passos necessários para chegar à saída é: {min_steps}")
