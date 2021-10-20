def count_sort(a):
    """Сортировка методом подсчета ([-10, 10])"""
    sort_list_beta = [0] * 21
    for i in a:
        sort_list_beta[int(i) + 10] += 1
    sort_list_alpha = []
    for index, number in enumerate(sort_list_beta):
        if sort_list_beta[index] > 0:
            sort_list_alpha.extend([index - 10] * number)

    return sort_list_alpha


massive = list(map(int, input().split()))
print(*count_sort(massive))
