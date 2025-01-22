import random


def cumsum(lst):
    cum_sum_nums = 0
    res_cum_nums_arr = []
    for num in lst:
        cum_sum_nums += num
        res_cum_nums_arr.append(cum_sum_nums)
    return res_cum_nums_arr


def weighted_choice(size, probs):
    res_cum_nums_arr = cumsum(probs)
    res_weighted_arr = []
    for i in range(size):
        r = random.uniform(0, 1)
        for i, c in enumerate(res_cum_nums_arr):
            if r <= c:
                res_weighted_arr.append(i)
                break
    return res_weighted_arr


print(weighted_choice(10, [0.1, 0.4, 0.2, 0.3]))
