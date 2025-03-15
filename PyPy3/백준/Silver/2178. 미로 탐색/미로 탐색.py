from collections import deque

N, M = map(int, input().split())

maze = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# 접근
# 1. BFS로 depth와 visited를 통해 처리
# 2. 진행 중 이미 이동 횟수가 최소치를 넘으렴 break

result = 10000

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue = deque([(0, 0, 1)])
visited[0][0] = 1
count = 1

while queue:
    px, py, depth = queue.popleft()

    for dx, dy in direction:
        nx, ny = px + dx, py + dy
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == '1' and visited[nx][ny] == 0:
            if nx == N-1 and ny == M-1:
                result = min(result, depth+1)
            else: 
                queue.append((nx, ny, depth + 1))
                visited[nx][ny] = 1

print(result)