'''
# fibonacci using for loop
n = int(input())
p1 = 1
p2 = 2
for i in range(n-3):

    nth = p1 + p2
    p1 = p2
    p2 = nth
print(nth)

'''
n = int(input())
p1 = 1
p2 = 1
i = 0
nth = 0
def fibo(p1, p2):
    global n, i, nth
    i = i + 1
    if i > n - 2:
        return nth
    nth = p1 + p2
    p1 = p2
    p2 = nth
    return fibo(p1, p2)

print(fibo(p1, p2))