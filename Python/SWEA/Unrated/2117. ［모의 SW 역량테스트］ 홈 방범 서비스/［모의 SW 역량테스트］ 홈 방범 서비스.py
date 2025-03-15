T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 집 좌표 미리 저장 (집이 있는 좌표만 저장)
    houses = [(i, j) for i in range(N) for j in range(N) if data[i][j] == 1]

    result = 0
    # 서비스 영역 k는 최대 2*N까지 고려 (맨해튼 거리가 최대 2*(N-1)까지 가능)
    max_k = 2 * N

    for i in range(N):
        for j in range(N):
            # 중심 (i, j)에서 각 맨해튼 거리 d에 해당하는 집의 개수를 저장
            count_by_distance = [0] * (2 * N - 1) # 수정된 부분
            for hx, hy in houses:
                d = abs(i - hx) + abs(j - hy)
                if d < 2 * N - 1: # 수정된 부분
                    count_by_distance[d] += 1
            # 누적합을 이용해 거리 d <= k-1 인 집의 수 계산
            cum = 0
            for k in range(1, max_k + 1):
                # k-1 거리에 해당하는 집을 누적
                if k - 1 < len(count_by_distance):
                    cum += count_by_distance[k - 1]
                # 운영 비용 계산: cost = k*k + (k-1)*(k-1)
                cost = k * k + (k - 1) * (k - 1)
                # 수익 = 집 수 * M 가 운영 비용 이상이면 손해가 아님
                if cum * M >= cost:
                    result = max(result, cum)

    print(f'#{tc} {result}')