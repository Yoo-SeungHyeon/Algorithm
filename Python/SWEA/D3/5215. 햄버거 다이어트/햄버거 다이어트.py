def DFS(idx, calorie_sum, taste_sum):
    global results
    if calorie_sum > L:
        return
    elif calorie_sum < L:
        if results < taste_sum:
            results = taste_sum

    for i in range(idx, N):
        select_taste = ingrediants[i][0]
        select_ingrediants = ingrediants[i][1]
        DFS(i+1, calorie_sum + select_ingrediants, taste_sum + select_taste)


T = int(input())

for tc in range(1, T+1):
    # N: 재료의 개수, L: 제한 칼로리
    N, L = map(int, input().split())

    ingrediants = []
    for _ in range(N):
        # (맛 점수, 칼로리)
        ingrediants.append(tuple(map(int, input().split())))

    results = 0
    DFS(0,0,0)
    print(f'#{tc} {results}')
