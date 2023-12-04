with open("input.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f]

res = 0
for x in lines:
    num = ""
    for i in range(len(x)):
        if x[i].isdigit():
            num += x[i]
            break
    for i in range(len(x)-1, -1, -1):
        if x[i].isdigit():
            num += x[i]
            break
    res += int(num)
print(res)

# Part 2

res = 0
for x in lines:
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(len(nums)):
        x = x.replace(nums[i], nums[i][0] + str(i+1) + nums[i][-1])

    num = ""
    for i in range(len(x)):
        if x[i].isdigit():
            num += x[i]
            break
    for i in range(len(x) - 1, -1, -1):
        if x[i].isdigit():
            num += x[i]
            break
    res += int(num)
print(res)


