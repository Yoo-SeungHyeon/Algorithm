import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N = 100,000, M = 1,000,000,000

array = sorted(list(map(int, input().split())))

if N < 2:
    print(0)

else:
    result = 0
    left = 0
    right = N - 1

    while left < right:
        if array[left] + array[right] < M:
            left += 1
        else:
            left += 1
            right -= 1
            result += 1

    print(result)