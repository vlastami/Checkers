sum = 0
print("N: ")
n = int(input())
i = 1

for i in range(n+1):
    sum = 0
    j = 1
    for j in range(i+1):
        sum += j*j
        print(str(j)+"^2", end='')
        if j != i:
            print("+", end='')
        else:
            print("=", end='')
    print(sum)