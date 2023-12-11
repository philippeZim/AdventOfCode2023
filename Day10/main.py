from collections import deque

with open("input.txt", "r") as f:
    lines = [l.rstrip() for l in f]


def helper1(i, j):
    of = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    res = []
    for k in range(len(of)):
        x = of[k]
        if i + x[0] < 0 or i + x[0] > (len(lines) - 1):
            continue
        if j + x[1] < 0 or j + x[1] > (len(lines[0]) - 1):
            continue
        new = [i + x[0], j + x[1]]
        newStr = str(new[0]) + " " + str(new[1])
        north = ["|", "7", "F"]
        east = ["-", "7", "J"]
        south = ["|", "L", "J"]
        west = ["-", "L", "F"]

        up = ["|", "L", "J", "S"]
        right = ["-", "F", "L", "S"]
        down = ["|", "F", "7", "S"]
        left = ["-", "7", "J", "S"]
        see = lines[new[0]][new[1]]
        see2 = lines[i][j]
        see3 = lines[2]
        if k == 0 and lines[new[0]][new[1]] in north and lines[i][j] in up:
            res.append(newStr)
        elif k == 1 and lines[new[0]][new[1]] in east and lines[i][j] in right:

            res.append(newStr)
        elif k == 2 and lines[new[0]][new[1]] in south and lines[i][j] in down:
            res.append(newStr)
        elif k == 3 and lines[new[0]][new[1]] in west and lines[i][j] in left:
            res.append(newStr)
    return res


def generate_graph():
    d = dict()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            nc = helper1(i, j)
            key = str(i) + " " + str(j)
            d[key] = nc
    return d


# graph contains: "3 5" : ["3 6", "4 5"]
graph = generate_graph()


def find_start():
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "S":
                return i, j
    return -1, -1


start = find_start()


def bfs(graph, s):
    # deque of tuples (num_of_steps, "i j")
    max_steps = 0
    start_str = str(s[0]) + " " + str(s[1])
    s = "0 " + start_str
    q = deque()
    q.append(s)

    visited = set(start_str)
    while q:
        cur_with_steps = q.popleft()
        cur_steps = int(cur_with_steps.split()[0])
        cur = cur_with_steps[cur_with_steps.find(" ") + 1:]

        for el in graph[cur]:

            if el in visited:
                continue
            if cur_steps + 1 > max_steps:
                max_steps = cur_steps + 1
            str_to_add = str(cur_steps + 1) + " " + el
            q.append(str_to_add)
            visited.add(el)
    return max_steps


test = bfs(graph, start)
print(test)


# Part 2

def bfs2(graph, s):
    # deque of tuples (num_of_steps, "i j")
    max_steps = 0
    start_str = str(s[0]) + " " + str(s[1])
    s = "0 " + start_str
    q = deque()
    q.append(s)

    visited = set()
    visited.add(start_str)
    while q:
        cur_with_steps = q.popleft()
        cur_steps = int(cur_with_steps.split()[0])
        cur = cur_with_steps[cur_with_steps.find(" ") + 1:]

        for el in graph[cur]:

            if el in visited:
                continue
            if cur_steps + 1 > max_steps:
                max_steps = cur_steps + 1
            str_to_add = str(cur_steps + 1) + " " + el
            q.append(str_to_add)
            visited.add(el)
    return visited


visited_visual = [[0] * len(lines[0]) for _ in range(len(lines))]

visited_set = bfs2(graph, start)

for x in visited_set:
    i = int(x.split()[0])
    j = int(x.split()[1])
    visited_visual[i][j] = 1

res = [[0] * len(lines[0]) for _ in range(len(lines))]


def inLoop(i, j):
    eg = 0
    for k in range(j):
        if visited_visual[i][k] == 1:
            if lines[i][k] in ["J", "L", "|"]:
                eg += 1
    if eg % 2 == 1:
        return True
    return False


for i in range(len(visited_visual)):

    for j in range(len(visited_visual[0])):
        if visited_visual[i][j] == 0:
            if inLoop(i, j):
                res[i][j] = 1

part2_res = 0
for x in res:
    for y in x:
        if y == 1:
            part2_res += 1
print(part2_res)
