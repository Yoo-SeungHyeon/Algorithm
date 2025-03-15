import sys

K = int(input())
stack = []
for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        del stack[-1]
    else:
        stack.append(n)
print(sum(stack))