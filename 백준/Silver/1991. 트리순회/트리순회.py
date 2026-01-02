import sys
sys.stdin = open("input.txt", "r")

from collections import defaultdict, deque

# 전위 순회
def clr_traversal(tree_dict: dict, node: str):
    if node == '.':
        return

    print(node, end="")

    left_child, right_child = tree_dict[node]
    clr_traversal(tree_dict, left_child)
    clr_traversal(tree_dict, right_child)



# 중위 순회
def lcr_traversal(tree_dict: dict, node: str):
    if node == '.':
        return

    left_child, right_child = tree_dict[node]
    lcr_traversal(tree_dict, left_child)
    print(node, end="")
    lcr_traversal(tree_dict, right_child)

# 후위 순회
def lrc_traversal(tree_dict: dict, node: str):
    if node == '.':
        return

    left_child, right_child = tree_dict[node]
    lrc_traversal(tree_dict, left_child)
    lrc_traversal(tree_dict, right_child)
    print(node, end="")


N = int(input())

tree = defaultdict(str)

for _ in range(N):
    parent, *child = input().split()

    tree[parent] = child

# print(tree)

clr_traversal(tree, 'A')
print("")
lcr_traversal(tree, 'A')
print("")
lrc_traversal(tree, 'A')
