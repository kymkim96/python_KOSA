import sys
sys.setrecursionlimit(1000000)
count_island = 0


def find_island(x, y):
    map_[x][y][1] = True
    # ↓
    if x < h - 1:
        if (map_[x + 1][y][1] == False) & (map_[x + 1][y][0] == 1):
            find_island(x + 1, y)
    # ↘
    if (x < h - 1) & (y < w - 1):
        if (map_[x + 1][y + 1][1] == False) & (map_[x + 1][y + 1][0] == 1):
            find_island(x + 1, y + 1)
    # →
    if y < w - 1:
        if (map_[x][y + 1][1] == False) & (map_[x][y + 1][0] == 1):
            find_island(x, y + 1)
    # ↗
    if (x > 0) & (y < w - 1):
        if (map_[x - 1][y + 1][1] == False) & (map_[x - 1][y + 1][0] == 1):
            find_island(x - 1, y + 1)
    # ↑
    if x > 0:
        if (map_[x - 1][y][1] == False) & (map_[x - 1][y][0] == 1):
            find_island(x - 1, y)
    # ↖
    if (x > 0) & (y > 0):
        if (map_[x - 1][y - 1][1] == False) & (map_[x - 1][y - 1][0] == 1):
            find_island(x - 1, y - 1)
    # ←
    if y > 0:
        if (map_[x][y - 1][1] == False) & (map_[x][y - 1][0] == 1):
            find_island(x, y - 1)
    # ↙
    if (x < h - 1) & (y > 0):
        if (map_[x + 1][y - 1][1] == False) & (map_[x + 1][y - 1][0] == 1):
            find_island(x + 1, y - 1)


result = []

while True:
    w, h = map(int, input().split())
    if (w == 0) & (h == 0):
        break
    map_ = [[[int(x), False] for x in input().split()] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if (map_[i][j][1] == False) & (map_[i][j][0] == 1):
                find_island(i, j)
                count_island += 1

    result.append(count_island)
    count_island = 0

for i in range(len(result)):
    print(result[i])