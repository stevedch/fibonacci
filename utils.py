def nth_succession(n):
    data = []
    a, b = 0, 1
    while a < n:
        data.append(a)
        a, b = b, a + b
    return data
