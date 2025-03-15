import sys
from collections import deque

input = sys.stdin.read
data = input().split()

idx = 0
T = int(data[idx])
idx += 1
results = []

for _ in range(T):
    n = int(data[idx])
    idx += 1
    prev_rank = list(map(int, data[idx:idx + n]))
    idx += n
    m = int(data[idx])
    idx += 1

    # 그래프 초기화
    adj_list = {i: [] for i in range(1, n + 1)}
    in_degree = {i: 0 for i in range(1, n + 1)}

    # 작년 순위 기준 그래프 생성
    for i in range(n):
        for j in range(i + 1, n):
            adj_list[prev_rank[i]].append(prev_rank[j])
            in_degree[prev_rank[j]] += 1

    # 상대적인 순위 변경 적용
    for _ in range(m):
        a, b = map(int, data[idx:idx + 2])
        idx += 2

        if b in adj_list[a]:  # 기존 a -> b를 b -> a로 변경
            adj_list[a].remove(b)
            adj_list[b].append(a)
            in_degree[b] -= 1
            in_degree[a] += 1
        else:  # 기존 b -> a를 a -> b로 변경
            adj_list[b].remove(a)
            adj_list[a].append(b)
            in_degree[a] -= 1
            in_degree[b] += 1

    # 위상 정렬 수행
    queue = deque()
    result = []

    # 진입 차수가 0인 노드 찾기
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    is_unique = True  # 유일한 순위인지 확인

    while queue:
        if len(queue) > 1:  # 유일한 정렬이 불가능하면 '?'
            is_unique = False
        curr = queue.popleft()
        result.append(curr)
        for neighbor in adj_list[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 결과 판별
    if len(result) != n:  # 싸이클 발생 -> 순위 결정 불가능
        results.append("IMPOSSIBLE")
    elif not is_unique:  # 유일한 순위가 아님 -> '?'
        results.append("?")
    else:
        results.append(" ".join(map(str, result)))

sys.stdout.write("\n".join(results) + "\n")
