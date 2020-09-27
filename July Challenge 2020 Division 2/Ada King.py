t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    l = []
    for i in range(8):
        for j in range(8):
            if (c >= n):
                l.append("X")
            else:
                l.append(".")
                c += 1
    m = 0
    l[0] = "O"
    for i in range(8):
        for j in range(8):
            print(l[m], end="")
            m += 1
        print()
