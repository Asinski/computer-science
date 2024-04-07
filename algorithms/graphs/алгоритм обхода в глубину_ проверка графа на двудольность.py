from sys import setrecursionlimit

setrecursionlimit(100000000)

#
#   2--0--6--7   1--9   5
#   |  |  |
#   3--4  8
#

n = 10

adj_list = [[2, 4, 6],
            [9],
            [0, 3],
            [2, 4],
            [0, 3],
            [],
            [0, 7, 8],
            [6],
            [6],
            [1]]

color = [0] * n
isBipartite = True


def dfs(v):
    for w in adj_list[v]:
        if color[w] == 0:
            color[w] = 3 - color[v]
            dfs(w)
        elif color[w] == color[v]:
            global isBipartite
            isBipartite = False


for i in range(n):
    if color[i] == 0:
        color[i] = 1
        dfs(i)

print(isBipartite)
