t = int(input())
for i in range(t):
    n = int(input())
    coins = []
    flag = 0
    l = list(map(int, input().split()))
    if (l[0] == 5):
        for i in range(0, n):
            if (l[i] == 5):
                coins.append(l[i])
            elif (l[i] == 10):
                if 5 in coins:
                    coins.remove(5)
                    coins.append(l[i])
                else:
                    print("NO")
                    flag = 1
                    break
            elif (l[i] == 15):
                if (coins.count(10) >= 1):
                    coins.remove(10)
                    coins.append(l[i])
                elif (coins.count(5) >= 2):
                    coins.remove(5)
                    coins.remove(5)
                    coins.append(l[i])
                else:
                    print("NO")
                    flag = 1
                    break
        if (flag == 0):
            print("YES")
    else:
        print("NO")


