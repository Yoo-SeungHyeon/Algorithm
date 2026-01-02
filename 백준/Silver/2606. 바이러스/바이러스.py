from collections import defaultdict, deque
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
M = int(input())

graph = defaultdict(list)
visited = [False] * (N + 1)
result = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
queue = deque([1])
visited[1] = True

while queue:
    now = queue.popleft()
    result += 1
    for child in graph[now]:
        if not visited[child]:
            queue.append(child)
            visited[child] = True

print(result - 1)