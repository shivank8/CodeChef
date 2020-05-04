t=int(input())
l=[]
for i in range(0,t):
    n=int(input())
    s=input()
    l.append(list(s.split()))
    min=n
    max=1
    flag=1
    for k in range(n):
        l[i][k] = int(l[i][k])
    for y in range(0,n-1):
        if (l[i][y+1] - l[i][y] <= 2):
            flag+=1
    if (flag==1):
        print("1 1")
        continue
    if (flag==n):
        print(n, n)
        continue
    for j in range(1,n-1):
        p=l[i][j]
        p2=l[i][j+1]
        P1=l[i][j-1]
        P=l[i][j]
        mx=1
        jt=j
        while(p2-p<=2 and p2-p>=0):
            mx+=1
            if (jt>=n-2):
                break
            p=p2
            p2=l[i][j+2]
            jt=jt+2
        jt=j
        while(P-P1<=2 and P-P1>=0):
            mx+=1
            if (jt<=2):
                break
            P=P1
            P1=l[i][j-2]
            jt=jt-2
        if(j==1):
            min=mx
        if(mx>max):
            max=mx
        if(mx<min):
            min=mx
    print(min,max)