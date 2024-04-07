from sys import setrecursionlimit

setrecursionlimit(100000000)


def eta(num_vertex, edges_list):
    adj_dict = dict.fromkeys(range(1, num_vertex + 1))
    for nv in range(1, num_vertex + 1):
        inter_list1 = list(filter(lambda x: nv in x, edges_list))
        inter_list2 = [item for sublist in inter_list1 for item in sublist]
        inter_list3 = sorted(list(filter(lambda y: y != nv, inter_list2)))
        adj_dict[nv] = inter_list3

    return adj_dict


def even(num_vertex, adj_list):
    for i in range(1, num_vertex + 1):
        if not len(adj_list[i]) % 2:
            continue
        else:
            return False
    return True


def band(num_vertex, adj_list):
    visited = dict.fromkeys(range(1, num_vertex + 1), False)
    num_components = 0

    def dfs(v, adj_list):
        visited[v] = True
        for w in adj_list[v]:
            if not visited[w]:
                dfs(w, adj_list)

    for v in range(1, num_vertex + 1):
        if not visited[v]:
            dfs(v, adj_list)
            num_components += 1

    return bool(num_components == 1)


def find_eulerian_tour(edges_list):
    stack = []
    tour = []

    stack.append(edges_list[0][0])

    while len(stack) > 0:
        v = stack[len(stack) - 1]

        degree = get_degree(v, edges_list)

        if degree == 0:
            stack.pop()
            tour.append(v)
        else:
            index, edge = get_edge_and_index(v, edges_list)
            edges_list.pop(index)
            stack.append(edge[1] if v == edge[0] else edge[0])

    return tour[1:]


def get_degree(v, edges_list):
    degree = 0
    for (x, y) in edges_list:
        if v in (x, y):
            degree += 1

    return degree


def get_edge_and_index(v, edges_list):
    for index, edge in enumerate(edges_list):
        if v in edges_list[index]:
            return index, edge


num_vertex, num_edge = map(int, input().split())
edges_list = [list(map(int, input().split())) for _ in range(num_edge)]

adj_list = eta(num_vertex, edges_list)

e = even(num_vertex, adj_list)
b = band(num_vertex, adj_list)

if all([e, b]):
    print(*find_eulerian_tour(edges_list)[::-1])
else:
    print("NONE")
