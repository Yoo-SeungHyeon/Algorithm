import sys

# 표준 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    강산이의 비밀번호를 알아내는 함수
    """
    key_input = input().strip()
    left_stack = []
    right_stack = []

    for char in key_input:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)
            
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))

T = int(input())
for _ in range(T):
    solve()
