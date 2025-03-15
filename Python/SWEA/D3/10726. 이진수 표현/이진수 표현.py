T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    n = int(N)
    m = int(M)
    binary = ''
    result = 'OFF'
    while m:
        binary = str(m%2) + binary
        m = m//2
    if binary[-n:] == '1'*n:
        result = 'ON'
    print(f'#{tc} {result}')