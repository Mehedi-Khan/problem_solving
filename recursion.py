# Remove triple quote to execute the file
"""
# fibonacci using for loop
n = int(input())
p1 = 1
p2 = 2
for i in range(n-3):

    nth = p1 + p2
    p1 = p2
    p2 = nth
print(nth)


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
# New Practice on recursion
def new_recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return new_recursion(n - 1) + new_recursion(n - 2)


print(new_recursion(10))

"""


