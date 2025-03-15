A = int(input())
B = int(input())
C = int(input())
ABC = A*B*C
abc = [i for i in str(ABC)]
for i in range(10):
    print(abc.count(str(i)))