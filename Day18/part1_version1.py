from PIL import Image

with open("in.txt", "r", encoding="utf-8") as f:
    lines = [l.rstrip().split() for l in f]


def max_width_and_height():
    max_l = 0
    max_r = 0
    max_u = 0
    max_d = 0
    width = 0
    height = 0

    for x in lines:
        d = x[0]
        n = int(x[1])
        if d == "R":
            width += n
            max_r = max(max_r, width)
        if d == "L":
            width -= n
            max_l = min(max_l, width)
        if d == "D":
            height += n
            max_d = max(max_d, height)
        if d == "U":
            height -= n
            max_u = min(max_u, height)
    return abs(max_l), max_r, abs(max_u), max_d


max_dimensions = max_width_and_height()
print(max_dimensions)
w = max_dimensions[0] + max_dimensions[1] + 1
h = max_dimensions[2] + max_dimensions[3] + 1
grid = [[0] * w for _ in range(h)]
print(f"width = {w}")
print(f"height = {h}\n")


def walk_grid():
    direct = {
        "U": (-1, 0),
        "R": (0, 1),
        "D": (1, 0),
        "L": (0, -1)
    }
    pos = (max_dimensions[2], max_dimensions[0])
    for x in lines:
        d = x[0]
        n = int(x[1])
        for _ in range(n):
            pos = (pos[0] + direct[d][0], pos[1] + direct[d][1])
            grid[pos[0]][pos[1]] = 1

walk_grid()

def valid(el):
    if el[0] < 0 or el[0] > len(grid) or grid[el[0]][el[1]] == 1:
        return False
    if el[1] < 0 or el[1] > len(grid[0]) or grid[el[0]][el[1]] == 1:
        return False
    return True
def bfs_fill():
    q = []
    q.append((20, 20))
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        cur = q.pop()
        for nd in d:
            new_el = (cur[0] + nd[0], cur[1] + nd[1])
            if valid(new_el):
                grid[new_el[0]][new_el[1]] = 1
                q.append(new_el)

bfs_fill()


def grid_to_image(grid, output_path):
    """
    Convert a grid of 0s and 1s to a black and white image.

    Parameters:
    - grid: A 2D list of integers (0 or 1).
    - output_path: The path where the image will be saved.

    Returns:
    - Saves the image at the specified path.
    """

    # Get the dimensions of the grid
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    # Create a new image in mode '1' (1-bit pixels, black and white)
    image = Image.new('1', (width, height))

    # Populate the image with data from the grid
    for y in range(height):
        for x in range(width):
            # Set the pixel value: 1 for white, 0 for black
            image.putpixel((x, y), grid[y][x])

    # Save the image
    image.save(output_path)

grid_to_image(grid, "./test.jpg")

def part1():
    res = 0
    for x in grid:
        for y in x:
            if y == 1:
                res += 1
    return res

print(part1())