setsize = 10
newset = [[] for _ in range(setsize)]


def add(x):
    if not find(x):
        newset[x % setsize].append(x)


def find(x):
    for now in newset[x % setsize]:
        if now == x:
            return True
    return False


def delete(x):
    xlist = newset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            # a, b = b, a - swap(a,b) - usual for C++
            # xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i]
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return
