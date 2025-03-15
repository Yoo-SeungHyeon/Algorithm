def dfs(depth, result, plus, minus, multi, div):
    global max_result, min_result

    # 모든 숫자를 사용했을 때 최댓값, 최솟값 갱신
    if depth == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    # 백트래킹: 남은 연산자가 있을 때만 수행
    if plus:
        dfs(depth + 1, result + nums[depth], plus - 1, minus, multi, div)
    if minus:
        dfs(depth + 1, result - nums[depth], plus, minus - 1, multi, div)
    if multi:
        dfs(depth + 1, result * nums[depth], plus, minus, multi - 1, div)
    if div:
        dfs(depth + 1, int(result / nums[depth]), plus, minus, multi, div - 1)  # Python 음수 나눗셈 처리

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    plus, minus, multi, div = map(int, input().split())
    nums = list(map(int, input().split()))

    # 결과값 초기화
    max_result = -100000000
    min_result = 100000000

    # DFS 탐색 시작
    dfs(1, nums[0], plus, minus, multi, div)

    print(f'#{tc} {max_result - min_result}')