import heapq


def heuristic(a, b):
    """
    Manhattan distance heuristic for A*
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(node, grid):
    """
    Returns valid neighboring cells (up, down, left, right)
    """
    rows, cols = grid.shape
    r, c = node
    candidates = [
        (r - 1, c),
        (r + 1, c),
        (r, c - 1),
        (r, c + 1)
    ]

    neighbors = []
    for nr, nc in candidates:
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 0:
            neighbors.append((nr, nc))
    return neighbors


def reconstruct_path(came_from, current):
    """
    Reconstructs the path from goal to start
    """
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(grid, start, goal):
    """
    A* pathfinding algorithm
    """
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors(current, grid):
            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []