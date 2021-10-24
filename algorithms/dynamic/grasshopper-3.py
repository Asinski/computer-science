def grasshopper(n, price: list):
    cost = [float("-inf"), price[1], price[1] + price[2]] + [0] * (n - 2)
    for i in range(3, n + 1):
        cost[i] = price[i] + min(cost[i - 1], cost[i - 2])

    path = [n]
    tmp = n
    while tmp > 1:
        if cost[tmp - 1] < cost[tmp - 2]:
            prev = tmp - 1
        else:
            prev = tmp - 2
        path.append(prev)
        tmp = prev

    return cost[n], path[::-1]


n = int(input())
price = list(map(float, input().split()))
print(grasshopper(n, price))
