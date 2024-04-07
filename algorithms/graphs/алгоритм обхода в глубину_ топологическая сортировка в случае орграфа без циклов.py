from sys import setrecursionlimit

setrecursionlimit(100000000)

n = 4

adj_list = [[1],
            [2],
            [3],
            []]

visited = [False] * n
ans = []


def dfs(v):
    visited[v] = True
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)
    ans.append(v)


for i in range(n):
    if not visited[i]:
        dfs(i)

print(*ans[::-1])
