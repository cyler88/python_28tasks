def fak(N):
    f = 1
    for i in range(1, N + 1):
        f = f * i
    return f


def squirrel(N):
    l = []
    l = list(str(fak(N)))
    return int(l[0])
