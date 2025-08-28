import sys
from collections import defaultdict

N = int(input())

pre_node = 0
result = [0]
num_idx = {i: 0 for i in range(N + 1)}

# print(num_idx)
for i in range(1, N + 1):
    node = int(input())

    if node - pre_node > 1:
        result = [-1, -1]
        break
    pre_node = node
    result.append(0)
    num_idx[node] = i
    result[num_idx[node - 1]] += 1

for i in range(1, len(result)):
    print(result[i])







