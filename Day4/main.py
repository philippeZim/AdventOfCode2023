# Part 1
with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

res = 0
for x in lines:
    y = x.split()
    ind = y.index("|")
    win = set(y[2:ind])
    pull = set(y[ind+1:])
    inter = win.intersection(pull)
    if len(inter) == 0:
        pre = 0
    else:
        pre = 2 ** (len(inter) - 1)

    res += pre
print(res)

# Part 2
preProcess = []
for x in lines:
    y = x.split()
    ind = y.index("|")
    win = set(y[2:ind])
    pull = set(y[ind+1:])
    inter = win.intersection(pull)
    preProcess.append([1, len(inter)])

for i in range(len(preProcess)):
    for k in range(preProcess[i][0]):
        for j in range(i + 1, i + 1 + preProcess[i][1]):
            preProcess[j][0] += 1

res = 0
for x in preProcess:
    res += x[0]
print(res)
