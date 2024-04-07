list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
i = j = 0
list_sort = []
while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:  # <= для устойчивости сортировки
        list_sort.append(list1[i])
        i += 1
    else:
        list_sort.append(list2[j])
        j += 1
list_sort += list1[i:] + list2[j:]
print(*list_sort)
