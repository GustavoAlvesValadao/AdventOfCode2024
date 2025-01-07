from collections import deque

def bfs(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

    if grid[start[1]][start[0]] == '#' or grid[end[1]][end[0]] == '#':
        return False
    
    queue = deque([start])
    visited = set([start]) 
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == end:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and (nx, ny) not in visited:
                if grid[ny][nx] == '.': 
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    return False 

def find_first_blocking_byte(byte_positions, grid, start, end):
    for i, (x, y) in enumerate(byte_positions):
        grid[y][x] = '#'

        if not bfs(grid, start, end):
            return (x, y)

    return None 

grid_size = 71 
grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

byte_positions = [
    (5, 4), (4, 2), (4, 5), (3, 0), (2, 1), (6, 3), (2, 4), (1, 5), (0, 6),
    (3, 3), (2, 6), (5, 1), (1, 2), (5, 5), (2, 5), (6, 5), (1, 4), (0, 4),
    (6, 4), (1, 1), (6, 1), (1, 0), (0, 5), (1, 6), (2, 0)
]

start = (0, 0)
end = (70, 70)

blocking_byte = find_first_blocking_byte(byte_positions, grid, start, end)
print(f"O primeiro byte que bloqueia o caminho é o {blocking_byte}")
