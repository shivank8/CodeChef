t = int(input())
for _ in range(t):
    n = int(input())
    l1 = []
    l2 = []
    for j in range(4 * n - 1):
        x, y = map(int, input().split())
        l1.append(x)
        l2.append(y)
    l1.sort()
    l2.sort()
    x2 = -1
    y2 = -1
    # print("l1",l1)
    # print("l2",l2)
    if (l1.count(l1[-1]) % 2 != 0):
        x2 = l1[-1]
    if (l2.count(l2[-1]) % 2 != 0):
        y2 = l2[-1]
    if (x2 == -1 or y2 == -1):
        for i in range(0, len(l1) - 1, 2):
            if (x2 == -1):
                if (l1[i] != l1[i + 1]):
                    x2 = l1[i]
            if (y2 == -1):
                if (l2[i] != l2[i + 1]):
                    y2 = l2[i]
            if (x2 != -1 and y2 != -1):
                break
    print(x2, y2)


