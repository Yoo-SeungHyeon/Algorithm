A = input()
B = input()
a = [i for i in A]
b = [j for j in B]
n = len(a) + len(b)
a_nd = list(set(a))
for i in a_nd:
    an = a.count(i)
    bn = b.count(i)
    if an >= bn:
        N = bn
    else:
        N = an
    n = n - 2*N
print(n)