t = int(input())
for _ in range(t):
    count = 0
    lst = list(input())
    i = 0
    while (i < len(lst) - 1):
        if ((lst[i] == 'x' and lst[i + 1] == 'y') or (lst[i] == 'y' and lst[i + 1] == 'x')):
            count += 1
            i += 2
        else:
            i += 1
    print(count)
