t = int(input())
for _ in range(t):
    sum = 0
    l = int(input())
    lst = list(map(int, input().split()))
    for i in range(0, l - 1):
        # print(abs(lst[i]-lst[i+1]))
        sum += abs(lst[i] - lst[i + 1]) - 1
    print(sum)

