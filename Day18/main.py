with open("in.txt", "r") as f:
    lines = [l.rstrip()[:l.find("(") - 1] for l in f]


def find_max_dir(l):
    cur = [0, 0]
    max_left = 0
    max_right = 0
    max_down = 0
    max_up = 0

    for x in l:
        n = int(x.split()[1])
        if x[0] == "L":
            cur[0] -= n
        elif x[0] == "R":
            cur[0] += n
        elif x[0] == "U":
            cur[1] += n
        elif x[0] == "D":
            cur[1] -= n
        else:
            print("Wrong Format")
            exit(1)

        max_left = min(cur[0], max_left)
        max_right = max(cur[0], max_right)
        max_down = min(cur[1], max_down)
        max_up = max(cur[1], max_up)

    return max_left, max_right, max_down, max_up


temp = find_max_dir(lines)

start_pos = (abs(temp[0]), temp[3])

line_len = abs(temp[0]) + 1 + temp[1]
num_of_lines = abs(temp[2]) + 1 + temp[3]

grid = [["."] * line_len for _ in range(num_of_lines)]

def mark_path()