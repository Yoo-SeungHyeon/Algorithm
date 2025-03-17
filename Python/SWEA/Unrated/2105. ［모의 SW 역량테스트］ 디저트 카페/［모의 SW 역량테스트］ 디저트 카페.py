# 대각선 이동 방향: 우하, 좌하, 좌상, 우상
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def find_max_desserts(N, grid):
    max_desserts = -1

    # 모든 시작점 탐색
    for i in range(N):
        for j in range(N):
            # 가능한 사각형 크기 (a: 첫 번째 변, b: 두 번째 변)
            for a in range(1, N):
                for b in range(1, N):
                    x, y = i, j
                    desserts = set()
                    path_valid = True

                    # 1. 우하 방향으로 a칸 이동
                    for _ in range(a):
                        nx, ny = x + dx[0], y + dy[0]
                        if not (0 <= nx < N and 0 <= ny < N) or grid[nx][ny] in desserts:
                            path_valid = False
                            break
                        desserts.add(grid[nx][ny])
                        x, y = nx, ny

                    # 2. 좌하 방향으로 b칸 이동
                    if path_valid:
                        for _ in range(b):
                            nx, ny = x + dx[1], y + dy[1]
                            if not (0 <= nx < N and 0 <= ny < N) or grid[nx][ny] in desserts:
                                path_valid = False
                                break
                            desserts.add(grid[nx][ny])
                            x, y = nx, ny

                    # 3. 좌상 방향으로 a칸 이동
                    if path_valid:
                        for _ in range(a):
                            nx, ny = x + dx[2], y + dy[2]
                            if not (0 <= nx < N and 0 <= ny < N) or grid[nx][ny] in desserts:
                                path_valid = False
                                break
                            desserts.add(grid[nx][ny])
                            x, y = nx, ny

                    # 4. 우상 방향으로 b칸 이동 (시작점 복귀)
                    if path_valid:
                        for _ in range(b):
                            nx, ny = x + dx[3], y + dy[3]
                            if not (0 <= nx < N and 0 <= ny < N) or grid[nx][ny] in desserts:
                                path_valid = False
                                break
                            desserts.add(grid[nx][ny])
                            x, y = nx, ny

                    # 시작점으로 돌아왔는지 확인
                    if path_valid and (x, y) == (i, j):
                        max_desserts = max(max_desserts, len(desserts))

    return max_desserts


# 입력 처리
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    result = find_max_desserts(N, grid)
    print(f"#{tc} {result}")