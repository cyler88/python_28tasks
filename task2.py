def odometer(N):
    d = 0
    for i in range(0, len(N), 2):
        d += N[i] 
    return d
