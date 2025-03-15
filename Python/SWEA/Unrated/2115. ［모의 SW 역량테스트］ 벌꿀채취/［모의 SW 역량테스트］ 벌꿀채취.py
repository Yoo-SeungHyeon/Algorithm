import time
from itertools import combinations

start = time.time()

def max_huny(i, j):
    target = data[i][j:j+M]

    if sum(target) <= C:
        return sum([t**2 for t in target])
    else:
        rst = 0
        for a in range(1 << len(target)):
            subset = []
            for b in range(len(target)):
                if a & (1 << b):
                    subset.append(target[b])
            if sum(subset) <= C:
                rst = max(rst, sum([s**2 for s in subset]))
        return rst


T = int(input())
for tc in range(1, T+1):
    # N*N 크기 벌통들, M: 선택 가능한 벌통 수, C: 채취 가능한 꿀의 최대량
    N, M, C = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    cal_data = []
    for x in range(N):
        for y in range(N-M+1):
            cal_data.append((x, y, max_huny(x, y)))
    result = 0
    for comba, combb in combinations(cal_data, 2):
        if comba[0] == combb[0] and abs(comba[1] - combb[1]) >= M:
            result = max(result, comba[2] + combb[2])
        elif comba[0] != combb[0]:
            result = max(result, comba[2] + combb[2])

    print(f'#{tc} {result}')

end = time.time()

print("총 소요 시간 : ", end - start)