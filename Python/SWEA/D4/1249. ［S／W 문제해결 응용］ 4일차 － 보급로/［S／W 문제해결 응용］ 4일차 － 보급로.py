from collections import deque

def BFS(N):
    queue = deque([(0, 0)])
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    check[0][0] = 0
    while queue:
        px, py = queue.popleft()
        now_value = check[px][py]
        for x, y in direction:
            nx, ny = px + x, py + y
            if 0 <= nx < N and 0 <= ny < N:
                child_value = int(road[nx][ny])
                if now_value + child_value < check[nx][ny]:
                    check[nx][ny] = now_value + child_value
                    queue.append((nx, ny))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = []
    for _ in range(N):
        road.append(list(input()))

    # check 배열 초기화 문제 해결: 리스트 컴프리헨션 사용
    check = [[9 * N * N + 1] * N for _ in range(N)] # 최대 비용 고려하여 초기값 설정

    BFS(N)

    print(f'#{tc} {check[N-1][N-1]}')