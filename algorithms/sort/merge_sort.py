

def merge_two_list(left, right):
    result_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result_list.append(left[i])
            i += 1
        else:
            result_list.append(right[j])
            j += 1
    result_list += left[i:] + right[j:]
    
    return result_list


def merge_sort(n):
    if len(n) == 1:
        return n
    middle = len(n) // 2
    left = merge_sort(n[:middle])
    right = merge_sort(n[middle:])

    return merge_two_list(left, right)


massive = list(map(int, input().split()))
print(*merge_sort(massive))
