# Part 1

with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f.readlines()]

races = []
times = [int(num) for num in lines[0].split()[1:]]
distances = [int(num) for num in lines[1].split()[1:]]
res = 1
for i in range(len(times)):
    temp = 0
    for j in range(1, times[i]):
        if (times[i] - j) * j > distances[i]:
            temp += 1
    res *= temp
print(res)

# Part 2

time = ""
distance = ""
for i in range(len(times)):
    time += str(times[i])
    distance += str(distances[i])
time = int(time)
distance = int(distance)
print(time, distance)
res2 = 0
for j in range(1, time):
    if (time - j) * j > distance:
        res2 += 1
print(res2)

