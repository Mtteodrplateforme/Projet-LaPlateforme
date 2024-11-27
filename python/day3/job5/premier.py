for i in range(2, 1001):
    x = True
    for diviseur in range(2, int(i ** 0.5) + 1):
        if i % diviseur == 0:
            x = False
            break
    if x:
        print(i)
