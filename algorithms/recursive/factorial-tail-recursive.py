def factorial(n, current_result=1):
    return current_result if n == 0 else factorial(n - 1, current_result * n)


n = int(input())
print(factorial(n))
