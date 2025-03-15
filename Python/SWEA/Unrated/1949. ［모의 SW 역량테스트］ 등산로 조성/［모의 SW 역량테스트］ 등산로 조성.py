# 상하좌우 이동
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, length, cut_used):
    global max_length
    max_length = max(max_length, length)
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # 일반 이동: 다음 셀이 현재 셀보다 낮은 경우
            if board[nx][ny] < board[x][y]:
                visited[nx][ny] = True
                dfs(nx, ny, length + 1, cut_used)
                visited[nx][ny] = False
            # 깎기를 사용할 수 있고, 깎아서 현재 셀보다 낮게 만들 수 있는 경우
            elif not cut_used and board[nx][ny] - K < board[x][y]:
                original = board[nx][ny]  # 원래 높이 저장
                board[nx][ny] = board[x][y] - 1  # 필요한 만큼 깎아서 이동 가능하게 만듦
                visited[nx][ny] = True
                dfs(nx, ny, length + 1, True)
                visited[nx][ny] = False
                board[nx][ny] = original  # 원상복구

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = []
    highest = 0

    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        highest = max(highest, max(row))
    
    # 최고 높이의 좌표 수집
    start_points = [(i, j) for i in range(N) for j in range(N) if board[i][j] == highest]
    
    max_length = 0
    visited = [[False] * N for _ in range(N)]
    
    # 모든 최고점에서 DFS 시작
    for x, y in start_points:
        visited[x][y] = True
        dfs(x, y, 1, False)
        visited[x][y] = False
    
    print(f'#{tc} {max_length}')
