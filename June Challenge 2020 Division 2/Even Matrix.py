t = int(input())
for i in range(t):
    m = int(input())
    n = 1
    sign = 1
    for j in range(m):
        for k in range(m):
            print(n,end=" ")
            n = n + sign
        print("")
        sign = sign * (-1)
        n += m + sign
