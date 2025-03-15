import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heap = []
    results = []
    for _ in range(N):
        calcul = input().split()
        if calcul[0] == '1':  # 첫 숫자가 1이면 heappush 수행
            heapq.heappush(heap, -int(calcul[1]))
        elif calcul[0] == '2':  # 첫 숫자가 2이면 heappop 수행
            if not heap:
                results.append(str(-1))
            else:
                results.append(str(-heapq.heappop(heap)))
    print(f'#{tc} {" ".join(results)}')