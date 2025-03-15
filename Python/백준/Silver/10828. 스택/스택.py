import sys
N = int(input())

stack = []
n=0
for _ in range(N):
    comm = list(sys.stdin.readline().split())
    match comm[0]:
        case 'push': 
            stack.append(int(comm[1]))
            n += 1
        case 'pop': 
            if n != 0 :
                print(stack.pop())
                n -= 1
            else: print(-1)
        case 'size': print(n)
        case 'empty':
            if n == 0 : print(1)
            else: print(0)
        case 'top': 
            if n != 0 :
                print(stack[-1])
            else: print(-1)