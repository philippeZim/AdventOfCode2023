lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()

temp = []
for i in range(len(lines)):
    if not i == len(lines) - 1:
        temp.append(lines[i][:-1])
    else:
        temp.append(lines[i])

lines = temp

grid = [[0] * len(lines[0]) for _ in range(len(lines))]

def helper(i, j, grid_len, first_el_len):
    res = [
        [i - 1, j - 1],
        [i - 1, j],
        [i - 1, j + 1],
        [i, j - 1],
        [i, j + 1],
        [i + 1, j - 1],
        [i + 1, j],
        [i + 1, j + 1]
    ]
    temp = []
    for x in res:
        if x[0] < 0 or x[1] < 0:
            continue
        if x[0] > grid_len - 1 or x[1] > first_el_len - 1:
            continue
        temp.append(x)
    return temp


for i in range(len(lines)):
    for j in range(len(lines[0])):
        if not lines[i][j].isdigit() and not lines[i][j] == ".":
            cur = helper(i, j, len(grid), len(grid[0]))
            for x in cur:
                grid[x[0]][x[1]] = 1


def arrToNum(arr):
    res = 0
    offset = 1
    for i in range(len(arr) - 1, -1, -1):
        res += arr[i] * offset
        offset *= 10
    return res


cur_num = []
toadd = False
res = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j].isdigit():
            cur_num.append(int(lines[i][j]))
            if grid[i][j] == 1:
                toadd = True
        else:
            if cur_num and toadd:
                num = arrToNum(cur_num)
                res += num
            cur_num = []
            toadd = False
print(res)

# Part 2

lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()

temp = []
for i in range(len(lines)):
    if i == len(lines) - 1:
        temp.append(lines[i])
    else:
        temp.append(lines[i][:-1])
lines = temp


def nums_positions(lines):
    cur_num = ""
    nums = []
    last = [0, 0]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if j == 0 and cur_num:
                nums.append([int(cur_num), last[0], last[1]])
                cur_num = ""
            elif lines[i][j].isdigit():
                cur_num += lines[i][j]
            else:
                if cur_num:
                    nums.append([int(cur_num), last[0], last[1]])
                    cur_num = ""
            last = [i, j]
    return nums


def digits(num):
    return len(str(abs(num)))


def mapNums(lines, num_pos):
    nums = [[[] for _ in range(len(lines[0]))] for _ in range(len(lines))]
    for x in num_pos:
        for i in range(x[1] - 1, x[1] + 2):
            for j in range(x[2] - 1 - (digits(x[0]) - 1), x[2] + 2):
                if i < 0 or j < 0:
                    continue
                try:
                    nums[i][j].append(x[0])
                except IndexError:
                    pass
    return nums


def resultCalc(lines):
    pos = nums_positions(lines)
    num_map = mapNums(lines, pos)
    res = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "*":
                gear = 1
                if len(num_map[i][j]) == 2:
                    for x in num_map[i][j]:
                        gear *= x
                    res += gear
    return res


test = resultCalc(lines)
print(test)
