def grasshopper(n, permit_stop: list):
    trajectories = [0, 1, int(permit_stop[2])] + [0] * (n - 2)
    for i in range(3, n + 1):
        if permit_stop[i]:
            trajectories[i] = trajectories[i - 1] + trajectories[i - 2]

    return trajectories[n]


n = int(input())
permit_stop = list(map(bool, map(int, input().split())))
print(grasshopper(n, permit_stop))
