def solution(n, lost, reserve):
    answer = 0
    
    students = [1] * (n + 1)
    for i in reserve:
        students[i] += 1
    
    for j in lost:
        students[j] -= 1
    
    for k in range(1, n+1, 1):
        if students[k] != 0:
            answer += 1
        elif k == 1:
            if students[2] == 2:
                answer += 1
        elif k == n:
            if students[n-1] == 2:
                answer += 1
        else:
            if students[k-1] == 2:
                answer += 1
                students[k-1] -= 1
            elif students[k+1] == 2:
                answer += 1
                students[k+1] -= 1

    return answer