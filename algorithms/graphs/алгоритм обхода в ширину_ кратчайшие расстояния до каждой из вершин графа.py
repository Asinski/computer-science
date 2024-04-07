def adj_vector(u, edges_list):
    a = list(filter(lambda x: u in x, edges_list))
    b = [item for sublist in a for item in sublist]
    c = sorted(list(filter(lambda y: y != u, b)))

    return c


def dfs(num_vertex, edges_list, start_vertex):
    distance_list = [None] * num_vertex

    distance_list[start_vertex] = 0
    queue = [start_vertex]
    queue_start = 0

    while queue_start < len(queue):
        u = queue[queue_start]
        queue_start += 1
        for v in adj_vector(u, edges_list):
            if distance_list[v] is None:
                distance_list[v] = distance_list[u] + 1
                queue.append(v)

    return distance_list


num_vertex, num_edge = map(int, input().split())
edges_list = [list(map(int, input().split())) for _ in range(num_edge)]
start_vertex = int(input())

print(*dfs(num_vertex, edges_list, start_vertex))