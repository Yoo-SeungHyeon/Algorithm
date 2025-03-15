T = 10

for tc in range(1, T+1):
    str_len = int(input())
    str = input()
    result = 0
    for char in str:
        if char != '+':
            result += int(char)
    print(f'#{tc} {result}')