def taste_sum(matrix, group):
    total_taste = 0
    for i in group:
        for j in group:
            total_taste += matrix[i][j]
    return total_taste
 
def solve(N, matrix):
    min_diff = float('inf')
 
    def find_combinations(index, current_group):
        nonlocal min_diff
 
        if len(current_group) == N // 2:
            other_group = [i for i in range(N) if i not in current_group]
            diff = abs(taste_sum(matrix, current_group) - taste_sum(matrix, other_group))
            min_diff = min(min_diff, diff)
            return
 
        if index == N:
            return
 
        # 현재 재료를 선택하는 경우
        find_combinations(index + 1, current_group + [index])
        # 현재 재료를 선택하지 않는 경우
        find_combinations(index + 1, current_group)
 
    find_combinations(0, [])
    return min_diff
 
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
 
    result = solve(N, matrix)
    print(f'#{tc} {result}')