N = input()
num = list(N)
num_count = []
for i in range(10):
    num_count.append(num.count(str(i)))
nine_six = (num_count[6] + num_count[9])//2 + (num_count[6] + num_count[9])%2
calc_num = num_count[0:6] + num_count[7:9] + [nine_six]
calc_num.sort(reverse=True)
print(calc_num[0])