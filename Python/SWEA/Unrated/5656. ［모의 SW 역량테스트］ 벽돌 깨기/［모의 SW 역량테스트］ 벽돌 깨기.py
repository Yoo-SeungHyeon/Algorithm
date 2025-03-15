from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# 각 열의 첫 번째 non-zero 블록의 좌표를 찾는 함수
def search_start(blocks):
    start_result = []
    for col_idx, col in enumerate(zip(*blocks)):
        found = False
        for row_idx, val in enumerate(col):
            if val != 0:
                start_result.append((row_idx, col_idx))
                found = True
                break
        if not found:
            start_result.append((None, col_idx))
    return start_result


# 블록 폭발 및 중력 적용 함수
def expolosion(blocks, point):
    # blocks의 깊은 복사 (원본 손상을 방지)
    new_blocks = [row[:] for row in blocks]
    H = len(new_blocks)
    W = len(new_blocks[0])

    queue = deque([point])
    while queue:
        h, w, value = queue.popleft()
        new_blocks[h][w] = 0  
        for v in range(1, value):
            for dx, dy in direction:
                nh, nw = h + dx * v, w + dy * v
                if 0 <= nh < H and 0 <= nw < W:
                    if new_blocks[nh][nw] == 1:
                        new_blocks[nh][nw] = 0
                    elif new_blocks[nh][nw] > 1:
                        nv = new_blocks[nh][nw]
                        new_blocks[nh][nw] = 0
                        queue.append((nh, nw, nv))

    # 재배치
    new_grid = [[0] * W for _ in range(H)]
    for col in range(W):
        stack = []
        for row in range(H):
            if new_blocks[row][col] != 0:
                stack.append(new_blocks[row][col])
        # 바닥부터 채우기
        row = H - 1
        while stack:
            new_grid[row][col] = stack.pop()
            row -= 1
    return new_grid


# 남은 블록 개수 세기
def count_block(blocks):
    count = 0
    for row in blocks:
        for val in row:
            if val != 0:
                count += 1
    return count


# DFS로 모든 경우의 수 탐색
def DFS(blocks, num):
    global results
    # 남은 블록이 없으면 바로 결과 갱신 후 종료
    if count_block(blocks) == 0:
        results = 0
        return

    if num == 0:
        results = min(results, count_block(blocks))
        return

    st_points = search_start(blocks)
    for st in st_points:
        # 시작 좌표가 None이거나, 범위를 벗어나면 건너뛰기
        if st[0] is None or st[0] >= len(blocks):
            continue
        if blocks[st[0]][st[1]] == 0:
            continue
        new_blocks = expolosion(blocks, (st[0], st[1], blocks[st[0]][st[1]]))
        DFS(new_blocks, num - 1)

T = int(input())
for tc in range(1, T + 1):
    # N: 구슬 수, W: 너비, H: 높이
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]

    results = 10000000
    DFS(blocks, N)
    print(f'#{tc} {results}')
