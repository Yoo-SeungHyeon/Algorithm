for tc in range(1,11):
    table_length = int(input())
    # 1 = N, 2 = S -> 1은 밑으로, 2는 위로
    table = []
    for _ in range(100):
        table.append(list(map(int, input().split())))
    result = 0
    for col in zip(*table):
        down = False
        up = False
        for mag in col:
            # down true and up true -> 교착 +1 -> down false, up false
            # down false and up true -> 그냥 사라짐. up false
            # down true and down true -> 그대로 down true
            # down false and down true -> down을 true로
            if mag == 1:
                down = True
            elif down and mag == 2:
                result += 1
                down = False
                up = False
            else: continue

    print(f'#{tc} {result}')