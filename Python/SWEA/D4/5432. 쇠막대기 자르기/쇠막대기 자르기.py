T = int(input())
for tc in range(1, T + 1):
    s = input()
    b = 0
    r = 0
    for i in range(len(s)):
        if s[i] == '(':
            b += 1
        elif s[i] == ')':
            b -= 1
            if s[i-1] == '(':
                r += b
            else:
                r += 1
    print(f'#{tc} {r}')