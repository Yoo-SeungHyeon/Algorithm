def solution(n, times):
    
    min_time = 1
    max_time = max(times) * n
    
    while min_time <= max_time:
        mid_time = (min_time + max_time)//2
        count = 0
        
        for time in times:
            count += mid_time//time
            if count > n:
                break
        
        if count < n:
            min_time = mid_time + 1
        else:
            max_time = mid_time - 1
    
    return min_time
