T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    gap = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if gap == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if gap + r1 > r2 and gap + r2 > r1:
            if gap < r1 + r2:
                print(2)
            elif gap == r1 + r2:
                print(1)
            else:
                print(0)
        elif gap + r1 == r2 or gap + r2 == r1:
            print(1)
        else:
            print(0)