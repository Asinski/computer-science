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

num_vertex, num_edge = map(int, input().split())
edges_list = [list(map(int, input().split())) for _ in range(num_edge)]

adj_list = eta(num_vertex, edges_list)

print(even(num_vertex, adj_list))