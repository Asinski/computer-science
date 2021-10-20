def grasshopper(n, price: list):
    cost = [float("-inf"), price[1], price[1] + price[2]] + [0] * (n - 2)
    for i in range(3, n + 1):
        cost[i] = price[i] + min(cost[i - 1], cost[i - 2])

    return cost[n]


n = int(input())
price = list(map(float, input().split()))
print(grasshopper(n, price))
