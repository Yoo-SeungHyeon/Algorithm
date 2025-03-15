struct = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (0, 1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)],
}

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    queue = [(R, C, 1)]
    visited[R][C] = 1
    result = 0
    while queue:
        px, py, depth = queue.pop(0)
        if depth > L:
            break
        result += 1

        for i, j in struct[tunnel[px][py]]:
            nx, ny = px + i, py + j # child가 가능한 좌표
            # child 인지 아닌지 조건으로 확인
            # 조건1 : 범위 내에 존재하는 nx, ny인가
            if 0 <= nx < N and 0 <= ny < M:
                # 조건2 : tunnel[nx][ny] 값이 0이 아닌가 & 방문한 적이 없는가
                if tunnel[nx][ny] and not visited[nx][ny]:
                    # 다 통과했으면 확실히 어떤 구조물이 있는 child 이다.
                    # 이제 연결되어 있는지 확인
                    if (-i, -j) in struct[tunnel[nx][ny]]:
                        # 방향이 반대이면 연결되어 있는 것
                        queue.append((nx, ny, depth+1))
                        visited[nx][ny] = 1

    print(f'#{tc} {result}')
