T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    len_A = len(A)
    len_B = len(B)
    cnt = A.count(B)
    result = len_A - (len_B - 1) * cnt
    print(f'#{tc} {result}')