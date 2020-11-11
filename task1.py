def fak(N):
    f = 1
    for i in range(1, N + 1):
        f = f * i
    return f


def first_number(N):
    l = []
    l = list(str(fak(N)))
    return l[0]


print(first_number(5))
