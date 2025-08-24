from collections import defaultdict

T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    v = list(map(int, input().split()))

    result = 0
    freq = defaultdict(int)

    for num in v:
        target = num ^ x

        result += freq[target]
        freq[num] += 1

    print(result)