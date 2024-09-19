with open("in.txt", "r", encoding="utf-8") as f:
    lines = [l.rstrip() for l in f]

# Part 1

inp = []
for x in lines:
    d = x.split()[0]
    n = int(x.split()[1])
    inp.append((d, n))


def calc_area(inp_l):
    map_dir = {
        "U": (-1, 0),
        "R": (0, 1),
        "D": (1, 0),
        "L": (0, -1)
    }

    position = (0, 0)

    # Dieser Teil nutzt die Gauß'sche Flächenformel und anschließend Pigs theorem

    res = 0
    b = 0
    for x in inp_l:
        b += x[1]
        last = position
        position = (position[0] + (map_dir[x[0]][0] * x[1]), position[1] + (map_dir[x[0]][1] * x[1]))
        res += last[1] * position[0] - last[0] * position[1]

    res /= 2
    res = int(res)
    i = res - (b / 2) + 1
    res = int(i + b)

    print(res)


calc_area(inp)

# Part 2

map2_dir = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U"
}
inp2 = []
for x in lines:
    n = int(x.split()[2][2:-2], 16)
    d = map2_dir[x.split()[2][-2:-1]]
    inp2.append((d, n))

calc_area(inp2)
