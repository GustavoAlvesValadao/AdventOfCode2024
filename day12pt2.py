from collections import deque

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
num_rows = len(grid)
num_cols = len(grid[0])

def in_bounds(rc):
    r, c = rc
    return (0 <= r < num_rows) and (0 <= c < num_cols)

def get_plant(rc):
    r, c = rc
    return grid[r][c]

def get_neighbors(rc):
    r, c = rc
    neighbors = []
    ds = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
    for (dr, dc) in ds:
        neighbors.append((r + dr, c + dc))
    return [n for n in neighbors if in_bounds(n)]

def get_plant_neighbors(rc):
    neighbors = get_neighbors(rc)
    return [n for n in neighbors if get_plant(n) == get_plant(rc)]

def get_region(rc):
    visited = set()
    region = set()
    queue = deque([rc])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            region.add(node)
            neighbors = get_plant_neighbors(node)
            unvisited_neighbors = [n for n in neighbors if n not in visited]
            queue.extend(unvisited_neighbors)
    return region

def calc_edges(region):
    edges = 0
    for (r, c) in region:
        north_n = (r - 1, c)
        west_n = (r, c - 1)
        nw_n = (r - 1, c - 1)
        if (north_n not in region):
            same_edge = (west_n in region) and (nw_n not in region)
            if not same_edge:
                edges += 1

        south_n = (r + 1, c)
        sw_n = (r + 1, c - 1)
        if south_n not in region:
            same_edge = (west_n in region) and (sw_n not in region)
            if not same_edge:
                edges += 1

        if west_n not in region:
            same_edge = (north_n in region) and (nw_n not in region)
            if not same_edge:
                edges += 1

        east_n = (r, c + 1)
        ne_n = (r - 1, c + 1)
        if east_n not in region:
            same_edge = (north_n in region) and (ne_n not in region)
            if not same_edge:
                edges += 1
    return edges

regions = []
visited = set()
for r in range(num_rows):
    for c in range(num_cols):
        rc = (r, c)
        if rc not in visited:
            region = get_region(rc)
            visited |= region
            regions.append(region)

total_price = 0
for region in regions:
    plant = get_plant(next(iter(region)))
    area = len(region)
    edges = calc_edges(region)
    price = area * edges
    total_price += price

print(total_price)
