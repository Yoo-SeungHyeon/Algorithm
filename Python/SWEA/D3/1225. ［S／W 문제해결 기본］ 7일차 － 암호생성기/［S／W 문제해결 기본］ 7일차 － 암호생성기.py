for _ in range(10):
    input()
    p = list(map(int, input().split()))
    i = -1
    n = 0
    while p[i]:
        i = (i + 1) % 8
        n = n % 5 + 1
        p[i] -= n
        if p[i] <= 0: p[i] = 0
    print(f'#{_+1} {" ".join(map(str, p[i+1:] + p[:i+1]))}')