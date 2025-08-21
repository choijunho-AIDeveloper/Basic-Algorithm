def solution(wallpaper):
    minW, minH, maxW, maxH = 1e9, 1e9, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                minW, minH, maxW, maxH = min(j, minW), min(i, minH), max(j, maxW), max(i, maxH)
    return [minH, minW, maxH + 1, maxW + 1]