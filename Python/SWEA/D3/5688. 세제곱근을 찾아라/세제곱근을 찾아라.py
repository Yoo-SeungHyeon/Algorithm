def find_cubed(num):
    result = 1
    while True:
        if result**3 == num:
            return result
        elif result**3 < num:
            result += 1
        else:
            return -1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    result = find_cubed(N)
    print(f'#{tc} {result}')