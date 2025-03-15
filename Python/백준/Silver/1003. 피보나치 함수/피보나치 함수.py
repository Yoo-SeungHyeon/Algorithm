def fibona_sum(n):
    fibo_list = [1, 0, 1]
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        for i in range(n-1):
            fibo_list.append(fibo_list[i+1] + fibo_list[i+2])
        return fibo_list[n],fibo_list[n+1]
    
T = int(input())

for _ in range(T):
    N = int(input())
    a,b = fibona_sum(N)
    print(a, b)