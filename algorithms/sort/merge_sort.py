

def merge_two_list(left, right):
    result_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= для устойчивости сортировки
            result_list.append(left[i])
            i += 1
        else:
            result_list.append(right[j])
            j += 1
    result_list += left[i:] + right[j:]
    
    return result_list


def merge_sort(a):
    if len(a) == 1:
        return a
    middle = len(a) // 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])

    return merge_two_list(left, right)


massive = list(map(int, input().split()))
print(*merge_sort(massive))
