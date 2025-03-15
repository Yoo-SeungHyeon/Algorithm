from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E, tnum1, tnum2 = map(int, input().split())
    data = list(map(int, input().split()))
    graph = dict()
    for i in range(0, E*2, 2):
        if graph.get(data[i]):
            graph[data[i]].append(data[i+1])
        else:
            graph[data[i]] = [data[i+1]]

    for j in range(1, E+2):
        if None == graph.get(j):
            graph[j] = []

    tnum1_parent = set()
    tnum2_parent = set()

    while not tnum1_parent&tnum2_parent:
        for k in range(1, E+1):
            if tnum1 in graph.get(k) :
                tnum1 = k
                tnum1_parent.add(k)
            elif tnum2 in graph.get(k):
                tnum2 = k
                tnum2_parent.add(k)

    result = list(tnum1_parent&tnum2_parent)[0]

    count = 0
    queue = deque([result])
    while queue:
        q = queue.popleft()
        count += 1
        for child in graph[q]:
            queue.append(child)

    print(f'#{tc} {result} {count}')