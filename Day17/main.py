from collections import deque

with open("input.txt", "r") as f:
    lines = [l.rstrip() for l in f]

graph_arr = []
for x in lines:
    temp = []
    for y in x:
        temp.append(int(y))
    graph_arr.append(temp)

graph = dict()
for i in range(len(graph_arr)):
    for j in range(len(graph_arr[0])):
        el = (i, j)
        neighbours = []
        if not (i == 0):
            neighbours.append((i - 1, j, graph_arr[i - 1][j]))
        if not (i == len(graph_arr) - 1):
            neighbours.append((i + 1, j, graph_arr[i + 1][j]))
        if not (j == 0):
            neighbours.append((i, j - 1, graph_arr[i][j - 1]))
        if not (j == len(graph_arr[0]) - 1):
            neighbours.append((i, j + 1, graph_arr[i][j + 1]))
        graph[el] = neighbours


def getPos(cur):
    res = []
    if cur[3] == 0:
        for x in graph[(cur[0], cur[1])]:
            if not (x[0] == cur[0] + 1 and x[1] == cur[1]):
                res.append(x)
    elif cur[3] == 1:
        for x in graph[(cur[0], cur[1])]:
            if not (x[0] == cur[0] and x[1] == cur[1] - 1):
                res.append(x)
    elif cur[3] == 2:
        for x in graph[(cur[0], cur[1])]:
            if not (x[0] == cur[0] - 1 and x[1] == cur[1]):
                res.append(x)
    elif cur[3] == 3:
        for x in graph[(cur[0], cur[1])]:
            if not (x[0] == cur[0] and x[1] == cur[1] + 1):
                res.append(x)
    return res


def a_star():
    q = deque()
    # x, y, accCost, move which Let to this pos (0=up, 1=right, 2=down, 3=left)
    start = (0, 0, 0, 1, "sss", "")
    dirm = {
        0: "u",
        1: "r",
        2: "d",
        3: "l"
    }
    q.append(start)
    seen = dict()
    seen[(start[0], start[1], 1)] = start[2]

    while q:
        print(len(seen))
        cur = q.popleft()
        #print(cur)
        #print(cur)

        pos = getPos(cur)
        if cur[5] == "112":
            print("t")

        for next in pos:
            if next[0] == cur[0] - 1 and next[1] == cur[1]:
                dirl = 0
            elif next[0] == cur[0] and next[1] == cur[1] + 1:
                dirl = 1
            elif next[0] == cur[0] + 1 and next[1] == cur[1]:
                dirl = 2
            else:
                dirl = 3
            co = (next[0], next[1], dirl)
            pdir = cur[4][1:] + dirm[dirl]

            if pdir == cur[4]:
                continue
            if co in seen:
                if seen[co] <= cur[2] + next[2] and dirm[dirl] == cur[5][-1]:
                    continue

            new = (next[0], next[1], cur[2] + next[2], dirl, pdir, cur[5] + str(dirl))
            q.append(new)
            seen[(next[0], next[1], dirl)] = cur[2] + next[2]

    return min(seen[(len(graph_arr) - 1, len(graph_arr[0]) - 1, 2)],
               seen[(len(graph_arr) - 1, len(graph_arr[0]) - 1, 1)])


print(a_star())
