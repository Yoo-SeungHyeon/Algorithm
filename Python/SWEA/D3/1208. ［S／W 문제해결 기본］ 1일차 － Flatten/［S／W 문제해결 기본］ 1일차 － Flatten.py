for tc in range(1,11):
    dump = int(input())
    boxs = list(map(int, input().split()))
    while dump and max(boxs) != min(boxs):
        max_index = boxs.index(max(boxs))
        min_index = boxs.index(min(boxs))
        boxs[max_index] -= 1
        boxs[min_index] += 1
        dump -= 1
    print(f'#{tc} {max(boxs) - min(boxs)}')