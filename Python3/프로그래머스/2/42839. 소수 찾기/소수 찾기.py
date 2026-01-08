from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    num_set = set()
    
    for i in range(1, len(numbers) + 1):
        permu_list = permutations(numbers, i)
        
        for p in permu_list:
            num = int("".join(p))
            num_set.add(num)
    
    answer = 0
    for num in num_set:
        if is_prime(num):
            answer += 1
            
    return answer