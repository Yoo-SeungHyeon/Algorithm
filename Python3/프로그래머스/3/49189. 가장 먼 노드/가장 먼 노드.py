from collections import deque, defaultdict

def solution(n, edge):
    
    graph = defaultdict(list);
    
    distances = [-1] * (n + 1)
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque([1])
    
    distances[1] = 0
    
    while q:
        ni = q.popleft()
        
        for i in graph[ni]:
            if (distances[i] == -1):
                q.append(i)
                distances[i] = distances[ni] + 1
        
    max_distance = max(distances)
    
    return distances.count(max_distance)