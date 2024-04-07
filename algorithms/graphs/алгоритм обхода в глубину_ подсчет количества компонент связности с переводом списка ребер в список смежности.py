from sys import setrecursionlimit
setrecursionlimit(100000000)

num_vertex, num_edge = map(int, input().split())
edges_list = [list(map(int, input().split())) for _ in range(num_edge)]
adj_dict = dict.fromkeys(range(1, num_vertex + 1))

for nv in range(1, num_vertex + 1):
    inter_list = []
    for ne in range(num_edge):
        if nv in edges_list[ne]:
            if nv == edges_list[ne][0]:
                inter_list.append(edges_list[ne][1])
            else:
                inter_list.append(edges_list[ne][0])
    adj_dict[nv] = inter_list

adj_list = list(map(sorted, list(adj_dict.values())))

visited = [False] * num_vertex
num_components = 0


def dfs(v):
    visited[v - 1] = True
    for w in adj_list[v - 1]:
        if not visited[w - 1]:
            dfs(w)


for v in range(1, num_vertex + 1):
    if not visited[v - 1]:
        dfs(v)
        num_components += 1

print(num_components)
