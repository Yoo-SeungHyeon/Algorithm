import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    result = 0
    max_stock = 0

    for i in range(N-1, -1, -1):
        # print(i)
        if stocks[i] > max_stock:
            max_stock = stocks[i]
        else:
            result += (max_stock - stocks[i])

    print(result)