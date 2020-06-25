n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
for i in l:
    t = i
    c = 0
    while (t % 2 == 0):
        t = t // 2
    if (t == 1):
        c = 0
    else:
        c = c + t // 2
    print(c)
