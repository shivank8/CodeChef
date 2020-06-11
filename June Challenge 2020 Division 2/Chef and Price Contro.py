t = int(input())
for i in range(t):
    n = int(input())
    coins = []
    c = 1
    l = list(map(int, input().split()))
    if (l[0] == 5):
        coins.append(l[0])
        for i in range(1, n):
            if (l[i] - 5) in coins:
                c += 1
                coins.remove(l[i] - 5)
                coins.append(l[i])
            elif l[i] == 5:
                c += 1
                coins.append(l[i])
        if c == n:
            print("YES")
        else:
            print('NO')
    else:
        print('NO')


