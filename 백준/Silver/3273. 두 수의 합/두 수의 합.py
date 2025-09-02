from collections import defaultdict

n = int(input())

arr = list(map(int, input().split()))

x = int(input())

check = defaultdict(int)

result = 0

for ar in arr:
    target = x - ar

    result += check[target]

    check[ar] += 1

print(result)