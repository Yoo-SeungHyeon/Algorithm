numbers = list(range(1000001))
prime_num = []
for num in numbers:
    if num != 0 and num != 1:
        prime_num.append(num)
        quo = 1000000//num
        for q in range(2, quo+1):
            numbers[num*q] = 0

T = int(input())

for tc in range(1, T + 1):
    D, A, B = map(int, input().split())
    result = 0
    for prime in prime_num:
        if prime >= A and prime <= B:
            if str(D) in str(prime):
                result += 1
    print(f'#{tc} {result}')