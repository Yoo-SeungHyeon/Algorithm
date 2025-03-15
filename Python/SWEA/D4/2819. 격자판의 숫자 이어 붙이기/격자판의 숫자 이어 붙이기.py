def dfs(grid, i, j, n, result, all_results):
    if not n:
        all_results.append(result)
        return

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for di, dj in directions:
        ni, nj = i + di, j + dj  # 이동한 좌표
        if 0 <= ni < 4 and 0 <= nj < 4:  # 격자판 범위 확인
            dfs(grid, ni, nj, n - 1, result + grid[ni][nj], all_results)


T = int(input())
for tc in range(1, T + 1):
    grid = []
    for _ in range(4):
        grid.append(input().split())
    temp = []
    for i in range(4):
        for j in range(4):
            dfs(grid, i, j, 7, '', temp)

    # 중복 제거
    temp.sort()
    result = [temp[i] for i in range(len(temp)) if i == 0 or temp[i] != temp[i - 1]]

    print(f'#{tc} {len(result)}')