class Node:
    def __init__(self, num, value, left = None, right = None): # left, right 기본값 지정
        self.num = int(num)
        self.value = value
        self.left = int(left) if left != None else None # None이면 그대로 아니면 정수로 변환
        self.right = int(right) if right != None else None # None이면 그대로 아니면 정수로 변환

def cal_graph(graph, index):
    node = graph[index]
    num1 = 0
    num2 = 0
    # left
    if node.left == None:
        return node.value
    else:
        num1 = int(cal_graph(graph, node.left))
    # right
    if node.right == None:
        return node.value
    else:
        num2 = int(cal_graph(graph, node.right))
    # value = 계산
    if node.value == '+':
        return num1 + num2
    elif node.value == '-':
        return  num1 - num2
    elif node.value == '*':
        return num1 * num2
    elif node.value == '/':
        return num1 / num2


for tc in range(1, 11):
    N = int(input())
    graph = [0]
    for _ in range(N):
        graph.append(Node(*input().split()))
    result = int(cal_graph(graph, 1))
    print(f'#{tc} {result}')