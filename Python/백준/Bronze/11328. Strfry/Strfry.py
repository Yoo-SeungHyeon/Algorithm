N = int(input())
result = []
for i in range(N):
    A,B = input().split()
    a = list(A)
    b = list(B)
    std = list(set(A))
    pf = []
    for j in std:
        if len(a) != len(b):
            pf.append('Impossible')
            break
        elif a.count(j) != b.count(j):
            pf.append('Impossible')
            break
        else:
            pf.append('Possible')
    if 'Impossible' in pf:
        result.append('Impossible')
    else:
        result.append('Possible')
for k in range(N):
    print(result[k])