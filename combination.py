# Program to find out all possible combination of items in a list
# used python


def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c + [a[0]]]
    return cs


cc = combs([1, 2, 3, 4, 5])

print(cc)
