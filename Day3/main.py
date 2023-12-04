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

def num_start_left(i, j):
	numStr = ""
	for k in range(j, len(lines[0])):
		if lines[i][k].isdigit():
			numStr += lines[i][k]
		else:
			break
	return int(numStr)

def num_start_right(i, j):
	numStr = ""
	for k in range(j, -1, -1):
		if lines[i][k].isdigit():
			numStr = lines[i][k] + numStr
		else:
			break
	return int(numStr)

def findLeft(i, j):
	k = j
	while(True):
		if k == 0:
			return 0
		if lines[i][k].isdigit():
			k -= 1
		else:
			return k + 1

def helper2(i, j):
	
	temp = [[0] * 3 for _ in range(3)]
	
	for k in range(i - 1, i + 2):
		for l in range(j - 1, j + 2):
			if k < 0 or l < 0:
				continue
			try:
				if lines[k][l].isdigit():
					temp[k - (i - 1)][l - (j - 1)] = 1
			except IndexError:
				pass
	
	numbers = 0
	if temp[0] == [1, 0, 0]:
		numbers += 1
	elif temp[0] == [0, 0, 1]:
		numbers += 1
	elif temp[0] == [1, 0, 1]:
		numbers += 2
	elif temp[0][1] == 1:
		numbers += 1
	
	if temp[1][0] == 1:
		numbers += 1
	if temp[1][2] == 1:
		numbers += 1
	
	if temp[2] == [1, 0, 0]:
		numbers += 1
	elif temp[2] == [0, 0, 1]:
		numbers += 1
	elif temp[2] == [1, 0, 1]:
		numbers += 2
	elif temp[2][1] == 1:
		numbers += 1
	
	if not numbers == 2:
		return -1
	
	prod = 1
	
	if temp[0] == [1, 0, 0]:
		prod *= num_start_right(i - 1, j - 1)
	elif temp[0] == [0, 1, 0]:
		prod *= int(lines[i - 1][j])
	elif temp[0] == [0, 0, 1]:
		prod *= num_start_left(i - 1, j + 1)
	elif temp[0] == [1, 0, 1]:
		prod *= num_start_right(i - 1, j - 1)
		prod *= num_start_left(i - 1, j + 1)
	elif temp[0] == [0, 1, 1]:
		prod *= num_start_left(i - 1, j)
	elif temp[0] == [1, 1, 0]:
		prod *= num_start_right(i - 1, j)
	elif temp[0] == [1, 1, 1]:
		prod *= num_start_left(i - 1, findLeft(i - 1, j - 1))
	
	
	if temp[1][0] == 1:
		prod *= num_start_right(i, j - 1)
	if temp[1][2] == 1:
		prod *= num_start_right(i, j + 1)
	
	if temp[2] == [1, 0, 0]:
		prod *= num_start_right(i + 1, j - 1)
	elif temp[2] == [0, 1, 0]:
		prod *= int(lines[i + 1][j])
	elif temp[2] == [0, 0, 1]:
		prod *= num_start_left(i + 1, j + 1)
	elif temp[2] == [1, 0, 1]:
		prod *= num_start_right(i + 1, j - 1)
		prod *= num_start_left(i + 1, j + 1)
	elif temp[2] == [0, 1, 1]:
		prod *= num_start_left(i + 1, j)
	elif temp[2] == [1, 1, 0]:
		prod *= num_start_right(i + 1, j)
	elif temp[2] == [1, 1, 1]:
		prod *= num_start_left(i + 1, findLeft(i + 1, j - 1))
	
	return prod


sum2 = 0
for i in range(len(lines)):
	for j in range(len(lines[0])):
		if lines[i][j] == "*":
			cur = helper2(i, j)
			if not cur == -1:
				sum2 += cur
print(sum2)
	
			