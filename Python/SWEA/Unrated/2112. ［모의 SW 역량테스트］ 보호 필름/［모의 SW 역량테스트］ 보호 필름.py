def check_film(film, D, W, K):
    """
    각 열마다 K개 이상 연속된 같은 셀이 있는지 검사합니다.
    하나라도 조건에 맞지 않으면 False를 리턴합니다.
    """
    for col in range(W):
        cnt = 1
        valid = False
        for row in range(1, D):
            if film[row][col] == film[row-1][col]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                valid = True
                break  # 이 열은 조건 만족하므로 다음 열로
        if not valid:
            return False
    return True

def dfs(row, cnt, film, D, W, K, ans):
    """
    DFS를 통해 각 행마다 약품 주입 여부(주입하지 않음, A 주입, B 주입)를 결정합니다.
    cnt: 현재까지 사용한 약품 수
    ans: [최소 약품 사용 수] (리스트에 담아 참조로 전달)
    """
    # 현재 사용한 약품 수가 이미 최소값보다 크거나 같으면 더 이상 진행하지 않음.
    if cnt >= ans[0]:
        return
    # 모든 행에 대해 처리한 경우, 필름의 성능 검사를 진행
    if row == D:
        if check_film(film, D, W, K):
            ans[0] = cnt
        return

    # 원본 행 저장 (복사본을 만들어 둡니다)
    original = film[row][:]

    # 1. 수정하지 않고 진행
    dfs(row + 1, cnt, film, D, W, K, ans)

    # 2. A 약품(0)을 주입 (해당 행 전체를 0으로 변경)
    film[row] = [0] * W
    dfs(row + 1, cnt + 1, film, D, W, K, ans)

    # 3. B 약품(1)을 주입 (해당 행 전체를 1로 변경)
    film[row] = [1] * W
    dfs(row + 1, cnt + 1, film, D, W, K, ans)

    # 재귀 호출 후 원래 상태로 복원
    film[row] = original

T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    
    # K가 1이면 어떤 필름이라도 통과하므로, 또는 이미 조건을 만족하면 약품 주입 필요 없음.
    if K == 1 or check_film(film, D, W, K):
        print(f'#{tc} 0')
    else:
        ans = [float('inf')]
        dfs(0, 0, film, D, W, K, ans)
        print(f'#{tc} {ans[0]}')
