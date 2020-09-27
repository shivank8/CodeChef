t = int(input())
for _ in range(t):
    n = int(input())
    golda = 0
    goldb = 0
    for q in range(n):
        g, a, b = map(int, input().split())
        time = (1 / a) + (1 / b)
        tm = (1 / time)
        # print("time",time)
        a1 = 1 / a
        ag = a1 * tm * g
        bg = (1 / b) * tm * g
        golda += ag
        goldb += bg
        # print("gold",golda,goldb)
    print('{0:.5f}'.format(golda), '{0:.5f}'.format(goldb))
