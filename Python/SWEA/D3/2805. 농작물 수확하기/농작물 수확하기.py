T = int(input())
for test_case in range(1, T+1):
    # 농장 크기
    size = int(input())
    # 농장 가치
    farm = []
    for _ in range(size):
        farm.append(input())
    # 중심 세팅
    center = size//2
    result = 0
    for i in range(size):
        if i <= center:
            for num in farm[i][center-i:center+i+1]:
                result += int(num)
        else:
            j = size-1- i
            for num in farm[i][center-j:center+j+1]:
                result += int(num)
    print(f'#{test_case} {result}')