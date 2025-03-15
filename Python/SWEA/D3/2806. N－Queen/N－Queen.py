# Q. N*N 보드에 N개의 퀸들 배치하는 경우의 수는 몇가지?

def check_place(deep_arr, i, j):
    direct = [(1,1),(-1,-1),(1,-1),(-1,1),(1,0),(-1,0),(0,1),(0,-1)]
    deep_arr[i][j] = 0
    arr_len = len(deep_arr)
    for k in range(arr_len):
        for dx, dy in direct:
            if 0<= i+dx*k < arr_len and 0 <= j+dy*k <arr_len:
                deep_arr[i + dx*k][j + dy*k] = 0
    return deep_arr


def n_queen(nn_arr, n):

    global result

    if n == len(nn_arr):
        result += 1
        return

    for j in range(len(nn_arr)):
        value = nn_arr[n][j]
        if value:
            new_arr = check_place([row[:] for row in nn_arr], n, j)
            n_queen(new_arr, n+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 1 <= N <= 10
    NN = [[1]*N for _ in range(N)]
    result = 0

    n_queen(NN, 0)

    print(f'#{tc} {result}')
