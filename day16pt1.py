import heapq

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'

def heuristic(x, y, end):
    return abs(x - end[0]) + abs(y - end[1])

def solve_maze(maze):

    start = end = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    pq = []
    heapq.heappush(pq, (heuristic(start[0], start[1], end), 0, start[0], start[1], 1))

    visited = set()

    while pq:
        _, cost, x, y, direction = heapq.heappop(pq)

        if (x, y) == end:
            return cost

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        if is_valid(nx, ny, maze) and (nx, ny, direction) not in visited:
            heapq.heappush(pq, (cost + 1 + heuristic(nx, ny, end), cost + 1, nx, ny, direction))

        new_direction = (direction + 1) % 4
        if (x, y, new_direction) not in visited:
            heapq.heappush(pq, (cost + 1000 + heuristic(x, y, end), cost + 1000, x, y, new_direction))

        new_direction = (direction - 1) % 4
        if (x, y, new_direction) not in visited:
            heapq.heappush(pq, (cost + 1000 + heuristic(x, y, end), cost + 1000, x, y, new_direction))

    return -1

maze = [
    "###############",
    "#.......#....E#",
    "#.#.###.#.###.#",
    "#.....#.#...#.#",
    "#.###.#####.#.#",
    "#.#.#.......#.#",
    "#.#.#####.###.#",
    "#...........#.#",
    "###.#.#####.#.#",
    "#...#.....#.#.#",
    "#.#.#.###.#.#.#",
    "#.....#...#.#.#",
    "#.###.#.#.#.#.#",
    "#S..#.....#...#",
    "###############"
]

maze = [list(row) for row in maze]

result = solve_maze(maze)
print(f"Pontuação mínima: {result}")
