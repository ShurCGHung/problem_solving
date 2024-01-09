def mygcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)

print(mygcd(30, 12))