# Dictionary and Has Mapping Problem Hacker Rank
# Link to problem : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

phone_book = {}

n = int(input())  # Number of entry to phone_book

# looping to input name and numbers to the phone book
for i in range(n):
    inp = input().split()
    phone_book[inp[0]] = int(inp[1])


# Query List
query = []
for j in range(n):
    query.append(input().strip())

# checking queries in the phone book
for item in query:
    if item in phone_book:
        print(f"{item}: {phone_book[item]}")
    else:
        print(f"Not found")
