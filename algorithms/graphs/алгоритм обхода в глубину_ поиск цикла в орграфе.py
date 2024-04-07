from sys import setrecursionlimit

setrecursionlimit(100000000)

n = 4

adj_list = [[1],
            [2],
            [3],
            [1]]

color = [0] * n
cycleFound = False


def dfs(v):
    color[v] = 1
    for w in adj_list[v]:
        if color[w] == 0:
            dfs(w)
        elif color[v] == 1:
            global cycleFound
            cycleFound = True
    color[v] = 2


for i in range(n):
    if color[i] == 0:
        dfs(i)

print(cycleFound)