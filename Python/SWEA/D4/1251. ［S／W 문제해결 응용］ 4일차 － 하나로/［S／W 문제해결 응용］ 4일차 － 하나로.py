T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    xp = list(map(int, input().split()))
    yp = list(map(int, input().split()))
    E = float(input())

    # MST에 포함되었는지 여부
    in_mst = [False] * N
    # 각 정점까지 MST에 연결될 때 필요한 최소 비용 (거리 제곱)
    min_edge = [float('inf')] * N
    min_edge[0] = 0  # 시작 정점은 비용 0

    total_cost = 0
    for _ in range(N):
        # 아직 MST에 포함되지 않은 정점 중 최소 비용 정점 선택
        u = -1
        curr_min = float('inf')
        for i in range(N):
            if not in_mst[i] and min_edge[i] < curr_min:
                curr_min = min_edge[i]
                u = i

        in_mst[u] = True
        total_cost += curr_min

        # 선택된 정점 u와 인접한 정점들의 최소 비용 갱신
        for v in range(N):
            if not in_mst[v]:
                cost = (xp[u] - xp[v]) ** 2 + (yp[u] - yp[v]) ** 2
                if cost < min_edge[v]:
                    min_edge[v] = cost

    # 최종 MST 비용에 환경 부담 세율 E를 곱하고 반올림
    print(f'#{tc} {round(total_cost * E)}')
