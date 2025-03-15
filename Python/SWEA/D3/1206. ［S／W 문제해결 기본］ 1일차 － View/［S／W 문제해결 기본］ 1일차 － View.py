for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0

    for idx in range(2, N-2):
        now = buildings[idx]
        left2 = max(buildings[idx-2:idx])
        right2 = max(buildings[idx+1:idx+3])
        if now > left2 and now > right2:
            result += (now - max(left2, right2))


    print(f'#{tc} {result}')