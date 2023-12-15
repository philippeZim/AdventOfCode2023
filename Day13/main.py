with open("input.txt", "r") as f:
    lines = [l.rstrip("\n") for l in f]

blocks = []
cur_block = []
for x in lines:
    if x == "":
        blocks.append(cur_block)
        cur_block = []
    else:
        cur_block.append(x)
blocks.append(cur_block)


def validCenter(block, lP, rP):
    while lP > -1 and rP < len(block):
        if block[lP] != block[rP]:
            return False
        rP += 1
        lP -= 1
    return True


def horizontal(block):
    d = dict()
    for i, y in enumerate(block):
        d[y] = d.get(y, ()) + (i,)
    for el in d:
        cur_arr = d[el]
        if len(cur_arr) > 1:
            for j in range(0, len(cur_arr) - 1):

                if cur_arr[j] + 1 == cur_arr[j + 1]:
                    if validCenter(block, cur_arr[j], cur_arr[j + 1]):
                        return cur_arr[j] + 1
    return -1


def transform_matrix(matrix):
    return [''.join(row) for row in zip(*matrix)]


res = 0
for i, x in enumerate(blocks):
    cur = horizontal(x)
    if cur == -1:
        cur = horizontal(transform_matrix(x))
    else:
        cur *= 100
    res += cur
print(res)

# Part 2

def horizontal2(block, last):
    d = dict()
    for i, y in enumerate(block):
        d[y] = d.get(y, ()) + (i,)
    for el in d:
        cur_arr = d[el]
        if len(cur_arr) > 1:
            for j in range(0, len(cur_arr) - 1):

                if cur_arr[j] + 1 == cur_arr[j + 1]:
                    if validCenter(block, cur_arr[j], cur_arr[j + 1]) and cur_arr[j] + 1 != last:
                        return cur_arr[j] + 1
    return -1

def changeOne(block, i, j):
    newBlock = []
    for k, x in enumerate(block):
        if k == i:
            if block[i][j] == "#":
                newBlock.append(x[:j] + "." + x[j + 1:])
            else:
                newBlock.append(x[:j] + "#" + x[j + 1:])
        else:
            newBlock.append(x)
    return newBlock


res2 = 0
for x in blocks:

    cur1 = horizontal(x)
    cur2 = horizontal(transform_matrix(x))

    quitt = False
    for i in range(len(x)):
        if quitt:
            break
        for j in range(len(x[0])):
            if i == 16 and j == 11:
                print()
            nb = changeOne(x, i, j)
            cur3 = horizontal2(nb, cur1)
            cur4 = horizontal2(transform_matrix(nb), cur2)

            if cur3 != -1 and cur3 != cur1:
                #print(cur3 * 100)
                res2 += cur3 * 100
                quitt = True
                break
            elif cur4 != -1 and cur4 != cur2:
                #print(cur4)
                res2 += cur4
                quitt = True
                break

print(res2)


