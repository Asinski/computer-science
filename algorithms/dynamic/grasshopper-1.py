def grasshopper(n):
    trajectories = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        trajectories[i] = trajectories[i - 1] + trajectories[i - 2]
        
    return trajectories[-1]


n = int(input())
print(grasshopper(n))
