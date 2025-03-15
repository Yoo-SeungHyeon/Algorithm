T = int(input())
for tc in range(1, T+1):
    N = int(input())
    elements = []
    for _ in range(N):
        x, y, m, e = map(int, input().split())
        elements.append([x*2, y*2, m, e])

    result = 0
    # 2000번 반복
    for _ in range(4000):
        # 좌표를 찍을 딕셔너리
        map_dict = {}
        crash = [] # 충돌이 발생한 좌표 확인
        # 모든 원자에 대해서
        for i in range(len(elements)):
            # 좌표 수정하고
            move_way = elements[i][2]
            if move_way == 0: elements[i][1] += 1
            if move_way == 1: elements[i][1] -= 1
            if move_way == 2: elements[i][0] -= 1
            if move_way == 3: elements[i][0] += 1

            # map_dict에 등록 하면서 중복 확인
            position = (elements[i][0], elements[i][1])
            if map_dict.get(position) == None:
                map_dict[position] = [i]
            else:
                map_dict[position] += [i]
                crash.append(position)
        new_list = []
        # crash가 발생한 모든 element의 energy 더하고 삭제
        if crash:
            crash = list(set(crash))
            for element in elements:
                for c in crash:
                    # print(crash)
                    p = (element[0], element[1])
                    if p == c:
                        # print(f'p: {p}, c: {c}')
                        result += element[3]
                    else:
                        new_list.append(element)
            elements = new_list
    print(f'#{tc} {result}')