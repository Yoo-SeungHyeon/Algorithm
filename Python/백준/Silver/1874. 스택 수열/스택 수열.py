import sys

n = int(input())

set = [a for a in range(n+4)]
cur = 0
result = []
i = 0
for _ in range(n):
    seq = int(sys.stdin.readline())
    while(1):
        if set[cur] < seq:
            result.append('+')
            cur += 1
        elif set[cur] == seq or set[cur] - seq == 1:
            result.append('-')     
            del set[cur]       
            cur -= 1
            break
        else:                        
            result.append('NO')
            break

if 'NO' in result:
    print('NO')
else:
    for j in result:
        print(j)