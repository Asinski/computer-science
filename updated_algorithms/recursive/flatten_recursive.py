def flatten_recursive(nst_lst):
    if not nst_lst:
        return []
    if isinstance(nst_lst[0], list):
        return flatten_recursive(nst_lst[0] + flatten_recursive(nst_lst[1:]))
    return nst_lst[:1] + flatten_recursive(nst_lst[1:])


assert flatten_recursive([1, [2, 3], [[4, [5]]]]) == [1, 2, 3, 4, 5]
