def DFS(start, total_sum):
    global result

    if total_sum == K:
        result += 1
        return
    if total_sum > K:
        return

    for i in range(start, N):
        selected = arr[i]
        DFS(i+1, total_sum+selected)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    # N개의 자연수로 합이 K가 되는 경우의 수 출력
    DFS(0,0)
    print(f'#{tc} {result}')