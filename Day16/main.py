from collections import deque

with open("input.txt", "r") as f:
    grid = [l.rstrip("\n") for l in f]


def isLegal(i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return True
    return False


def move(node):
    res = []
    newI = node[0] + node[2]
    newJ = node[1] + node[3]

    if isLegal(newI, newJ):
        if grid[newI][newJ] == "/":
            res.append((newI, newJ, -node[3], -node[2]))  # Reflect 90 degrees
        elif grid[newI][newJ] == "\\":
            res.append((newI, newJ, node[3], node[2]))  # Reflect 90 degrees
        elif grid[newI][newJ] == "-" and node[3] == 0:
            res.append((newI, newJ, 0, 1))
            res.append((newI, newJ, 0, -1))
        elif grid[newI][newJ] == "|" and node[2] == 0:
            res.append((newI, newJ, 1, 0))
            res.append((newI, newJ, -1, 0))
        else:
            res.append((newI, newJ, node[2], node[3]))

    return res


def bfs(graph, node):
    q = deque()
    q.append(node)
    visited = set()

    # node = (pos1, pos2, dir1, dir2)

    while q:
        cur = q.popleft()
        for next in move(cur):
            if next in visited:
                continue

            q.append(next)
            visited.add(next)
    return visited


marked = bfs(grid, (0, -1, 0, 1))

res = 0
see = [['.' for _ in x] for x in grid]

for x, y, _, _ in marked:
    if see[x][y] == '.':
        see[x][y] = '#'
        res += 1


"""
Visualization

for row in see:
    print(''.join(row))
"""

print(res)

# Part 2

maxLight = 0

for i in range(len(grid[0])):
    marked = bfs(grid, (-1, i, 1, 0))

    posSet = set()
    for x in marked:
        posSet.add((x[0], x[1]))
    if len(posSet) > maxLight:
        maxLight = len(posSet)

for i in range(len(grid[0])):
    marked = bfs(grid, (len(grid), i, -1, 0))

    posSet = set()
    for x in marked:
        posSet.add((x[0], x[1]))
    if len(posSet) > maxLight:
        maxLight = len(posSet)

for i in range(len(grid)):
    marked = bfs(grid, (i, -1, 0, 1))

    posSet = set()
    for x in marked:
        posSet.add((x[0], x[1]))
    if len(posSet) > maxLight:
        maxLight = len(posSet)

for i in range(len(grid)):
    marked = bfs(grid, (i, len(grid[0]), 0, -1))

    posSet = set()
    for x in marked:
        posSet.add((x[0], x[1]))
    if len(posSet) > maxLight:
        maxLight = len(posSet)

print(maxLight)
