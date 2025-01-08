def dfs(grid, i, j, visited, region):
    m, n = len(grid), len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    stack = [(i, j)]
    visited[i][j] = True
    region.append((i, j))

    while stack:
        x, y = stack.pop()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
                visited[nx][ny] = True
                stack.append((nx, ny))
                region.append((nx, ny))

def calculate_perimeter(grid, region):
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x, y in region:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != grid[x][y]:
                perimeter += 1

    return perimeter

def garden_plots(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]

    regions = []

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                region = []
                dfs(grid, i, j, visited, region)
                regions.append(region)

    result = []
    for region in regions:
        area = len(region)
        perimeter = calculate_perimeter(grid, region)
        result.append((area, perimeter))

    return result

grid = [
    ['R','R','R','R','I','I','C','C','F','F'],
    ['R','R','R','R','I','I','C','C','C','F'],
    ['V','V','R','R','R','C','C','F','F','F'],
    ['V','V','R','C','C','C','J','F','F','F'],
    ['V','V','V','V','C','J','J','C','F','E'],
    ['V','V','I','V','C','C','J','J','E','E'],
    ['V','V','I','I','I','C','J','J','E','E'],
    ['M','I','I','I','I','I','J','J','E','E'],
    ['M','I','I','I','S','I','J','E','E','E'],
    ['M','M','M','I','S','S','J','E','E','E'],
  ]


regions_info = garden_plots(grid)

total = 0

for area, perimeter in regions_info:
    total += area * perimeter
    print(f"Área: {area}, Perímetro: {perimeter}")

print(f"Soma total de Área * Perímetro: {total}")
