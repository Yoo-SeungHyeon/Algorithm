class Node:
    def __init__(self, num, value, left = None, right = None):
        self.num = int(num)
        self.value = value
        self.left = int(left) if left != None else None
        self.right = int(right) if right != None else None


def in_order(graph: list, index: int):
    left = graph[index].left
    right = graph[index].right
    value = graph[index].value

    if left == None:
        print(value, end='')
        return
    else:
        in_order(graph, left)

    if right == None:
        print(value, end='')
        return
    else:
        print(value, end='')
        in_order(graph, right)

for tc in range(1, 11):
    N = int(input())
    graph = [0]
    for _ in range(N):
        graph.append(Node(*input().split()))
    print(f'#{tc}', end=' ')
    in_order(graph, 1)
    print()