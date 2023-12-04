lines = []
with open("input.txt", "r") as f:
	lines = f.readlines()

sum = 0
for i, x in enumerate(lines):
	cur = x.split()
	game = int(cur[1][:-1])
	r, g, b = 0, 0, 0
	valid = True
	for j in range(2, len(cur), 2):
		
		if "red" in cur[j + 1]:
			r += int(cur[j])
		elif "green" in cur[j + 1]:
			g += int(cur[j])
		else:
			b += int(cur[j])
		if r > 12 or g > 13 or b > 14:
			valid = False
			break
		if ";" in cur[j + 1]:
			r, g, b = 0, 0, 0
	if valid:
		sum += game
			
print(sum)

# Part 2

sum = 0
for i, x in enumerate(lines):
	cur = x.split()
	rm, gm, bm = 0, 0, 0
	r, g, b = 0, 0, 0
	for j in range(2, len(cur), 2):
		
		if "red" in cur[j + 1]:
			r += int(cur[j])
		elif "green" in cur[j + 1]:
			g += int(cur[j])
		else:
			b += int(cur[j])
		if ";" in cur[j + 1]:
			if r > rm:
				rm = r
			if g > gm:
				gm = g
			if b > bm:
				bm = b
			r, g, b = 0, 0, 0
	if r > rm:
		rm = r
	if g > gm:
		gm = g
	if b > bm:
		bm = b
	power = rm * gm * bm
	sum += power
			
print(sum)

