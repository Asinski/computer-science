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

visited = [False] * n
component = [0] * n
num_components = 0


def dfs(v):
    component[v] = num_components + 1
    visited[v] = True
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)


for v in range(n):
    if not visited[v]:
        dfs(v)
        num_components += 1

i, j = map(int, input().split())
if component[i] == component[j]:
    print(True)
else:
    print(False)
