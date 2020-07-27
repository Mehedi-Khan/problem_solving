# Printing pattern using Recursion

def printer(d, i):
    if i >= 100:
        return 'd' * 100
    print(d * i)
    return printer(d, i + 1)


i = 1
printer('d', i)

j = 100


def printer2(d, j):
    if j == 1:
        print(d)
    else:
        print(d * j)
        return printer2(d, j - 1)


printer2('d', 100)
