for k in range(n):
    l[i][k] = int(l[i][k])
for j in range(0, n - 1):
    if (l[i][j + 1] - l[i][j] <= 2):
        flag += 1

if (flag == 1):
    print("1 1")
if (flag == n):
    print(n, n)