def get_num(str):
    if str == '0001101':
        return 0
    elif str == '0011001':
        return 1
    elif str == '0010011':
        return 2
    elif str == '0111101':
        return 3
    elif str == '0100011':
        return 4
    elif str == '0110001':
        return 5
    elif str == '0101111':
        return 6
    elif str == '0111011':
        return 7
    elif str == '0110111':
        return 8
    elif str == '0001011':
        return 9

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    data = []
    for _ in range(N):
        temp = input()
        for t in temp:
            if t == '1':
                data=temp
                break
    target = ''
    for i in range(1, M+1):
        if data[-i] == '1':
            target = data[-i-55:-i+1]
            break
    solve_data = []
    for j in range(8):
        solve_data.append(get_num(target[j*7:j*7+7]))
    check = 0
    result = 0
    for i in range(8):
        if i % 2 == 0:
            check += solve_data[i]*3
            result += solve_data[i]
        else:
            check += solve_data[i]
            result += solve_data[i]
    if check %10 == 0:
        print(f'#{test_case} {result}')
    else:
        print(f'#{test_case} 0')
