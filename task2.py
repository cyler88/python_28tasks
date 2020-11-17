def odometer(N):
    chet = [i for i in range(len(N)) if not i % 2]
    nechet = [i for i in range(len(N)) if i % 2]
    D = 0
    for i in range(len(chet)):
        if i == 0:
            D += N[chet[i]] * N[nechet[i]]
        else:
            D += (N[chet[i]] * (N[nechet[i]] - N[nechet[i - 1]]))
    return D
