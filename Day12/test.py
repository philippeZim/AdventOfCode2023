def getLines():
    with open("input.txt", "r") as f:
        lines = [line.rstrip("\n") for line in f]

    strings = []
    checks = []
    for x in lines:
        see = x
        strings.append(x.split()[0])
        checks.append([int(toint) for toint in x.split()[1].split(",")])

    return list(zip(strings, checks))


lines = getLines()


def tup_valid(tup, check):
    check_sum = sum(check)
    if len(tup[1]) > len(check):
        return False
    if len(tup[1]) < len(check) and tup[2] > check[len(tup[1])]:
        return False
    if tup[3] > check_sum:
        return False
    for i, x in enumerate(tup[1]):
        if x != check[i]:
            return False
    if tup[4] < check_sum - tup[3]:
        return False
    return True


def solve(line):
    s = line[0] + "."
    check = line[1]
    all_list = []
    max_hash = s.count("#") + s.count("?")
    all_list.append(("", [], 0, 0, max_hash))
    for i in range(len(s)):
        new_all_list = []
        for j in range(len(all_list)):
            print("! " + str(len(all_list)))
            if s[i] == ".":
                new_for_point = (all_list[j][0] + ".", all_list[j][1], 0, all_list[j][3], all_list[j][4])
                if tup_valid(new_for_point, check):
                    new_all_list.append(new_for_point)
            elif s[i] == "#":
                if i < len(s) - 1 and s[i + 1] == ".":
                    new_groups = all_list[j][1].copy()
                    new_groups.append(all_list[j][2] + 1)
                    new_for_hash1 = (all_list[j][0] + "#", new_groups, 0, all_list[j][3] + 1, all_list[j][4] - 1)
                    if tup_valid(new_for_hash1, check):
                        new_all_list.append(new_for_hash1)
                else:
                    new_for_hash2 = (all_list[j][0] + "#", all_list[j][1], all_list[j][2] + 1,
                                     all_list[j][3] + 1, all_list[j][4] - 1)
                    if tup_valid(new_for_hash2, check):
                        new_all_list.append(new_for_hash2)
            else:
                if i != 0 and all_list[j][0][i - 1] == "#":
                    new_groups2 = all_list[j][1].copy()
                    new_groups2.append(all_list[j][2])
                    new_for_point = (all_list[j][0] + ".", new_groups2, 0, all_list[j][3], all_list[j][4] - 1)
                else:
                    new_for_point = (all_list[j][0] + ".", all_list[j][1], 0,
                                     all_list[j][3], all_list[j][4] - 1)

                if tup_valid(new_for_point, check):
                    new_all_list.append(new_for_point)

                if i < len(s) - 1 and s[i + 1] == ".":
                    new_groups = all_list[j][1].copy()
                    new_groups.append(all_list[j][2] + 1)
                    new_for_hash1 = (all_list[j][0] + "#", new_groups, 0, all_list[j][3] + 1, all_list[j][4] - 1)
                    if tup_valid(new_for_hash1, check):
                        new_all_list.append(new_for_hash1)
                else:
                    new_for_hash2 = (all_list[j][0] + "#", all_list[j][1], all_list[j][2] + 1,
                                     all_list[j][3] + 1, all_list[j][4] - 1)
                    if tup_valid(new_for_hash2, check):
                        new_all_list.append(new_for_hash2)

        all_list = new_all_list.copy()
    return len(all_list)

# ?.??.??###??.#.?? 1,1,4,1,1
t = solve(("?.??.??###??.#.??", [1,1,4,1,1]))
with open("Save.txt", "r") as f:
    comp_res = [l.rstrip("\n") for l in f]

res = 0
for i, line in enumerate(lines):
    print(i)
    str2 = ((line[0] + "?") * 5)[:-1]
    check2 = []
    for _ in range(5):
        for x in line[1]:
            check2.append(x)
    part2_line = (str2, check2)
    curRes = solve(part2_line)
    res += curRes
print(res)

