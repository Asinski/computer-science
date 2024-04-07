def flatten(nst_lst):
    if not nst_lst:
        return []

    if isinstance(nst_lst[0], list):
        return flatten(nst_lst[0] + flatten(nst_lst[1:]))
    return nst_lst[:1] + flatten(nst_lst[1:])
