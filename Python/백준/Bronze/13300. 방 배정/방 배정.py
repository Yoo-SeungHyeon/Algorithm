N, K = map(int,input().split())
room = [[0 for i in range(2)] for j in range(6)]
for i in range(N):
    a,b = map(int,input().split())
    room[b-1][a] = int(room[b-1][a]) + 1
rnum = 0
for j in range(6):
    for l in range(2):
        rnum = rnum + room[j][l]//K
        if room[j][l]%K != 0:
            rnum = rnum + 1
print(rnum)