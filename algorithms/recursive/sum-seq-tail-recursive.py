def sum_tail_recursive(n, current_result=0):
    return current_result if n == 0 else sum_tail_recursive(n - 1, current_result + n)


n = int(input())
print(sum_tail_recursive(n))
