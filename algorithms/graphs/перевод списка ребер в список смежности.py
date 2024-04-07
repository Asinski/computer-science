def eta(num_vertex, edges_list):
    adj_list = dict.fromkeys(range(1, num_vertex + 1))
    for nv in range(1, num_vertex + 1):
        inter_list1 = list(filter(lambda x: nv in x, edges_list))
        inter_list2 = [item for sublist in inter_list1 for item in sublist]
        inter_list3 = sorted(list(filter(lambda y: y != nv, inter_list2)))
        adj_list[nv] = inter_list3

    return adj_list


num_vertex, num_edge = map(int, input().split())
edges_list = [list(map(int, input().split())) for _ in range(num_edge)]

print(eta(num_vertex, edges_list))
