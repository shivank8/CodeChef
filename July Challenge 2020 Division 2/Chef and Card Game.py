t = int(input())
for _ in range(t):
    l = int(input())
    ca = 0
    cb = 0
    count = 0
    for i in range(l):
        sa = 0
        sb = 0
        a, b = map(int, input().split())
        while (a > 0):
            # print("d",a%10)
            sa += a % 10
            a = a // 10
        while (b > 0):
            sb += b % 10
            b = b // 10
        if (sa > sb):
            ca += 1
        elif (sb > sa):
            cb += 1
        else:
            ca += 1
            cb += 1
    if (ca > cb):
        print(0, ca)
    elif (cb > ca):
        print(1, cb)
    else:
        print(2, ca)




