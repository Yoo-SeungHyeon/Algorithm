import heapq

def solution(operations):
    q = []
    
    for oper in operations:
        command, num = oper.split()
        num = int(num)
        
        if (command == "I"):
            heapq.heappush(q, num)
        elif (command == "D"):
            if not q:
                continue
            
            if (num == 1):
                q.remove(max(q))
            else: heapq.heappop(q)

    if not q:
        return [0, 0]
    else:
        return [max(q), heapq.heappop(q)]