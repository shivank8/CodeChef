for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if a==b:
        print(0)
    else:
        ra = []
        rb = []
        nra = []
        nrb = []
        i = 0
        while i<n-1:
            if a[i]==a[i+1]:
                ra.append(a[i])
                i+=2
            else:
                nra.append(a[i])
                i+=1
        if i==n-1:
            nra.append(a[i])
        i = 0
        while i<n-1:
            if b[i]==b[i+1]:
                rb.append(b[i])
                i+=2
            else:
                nrb.append(b[i])
                i+=1
        if i==n-1:
            nrb.append(b[i])
        if nra!=nrb:
            print(-1)
        else:
            dda = {}
            ddb = {}
            for i in ra:
                if i in dda:
                    dda[i]+=1
                else:
                    dda[i] = 1
            for i in rb:
                if i in ddb:
                    ddb[i]+=1
                else:
                    ddb[i] = 1
            rra = []
            rrb = []
            for i in set(ra+rb):
                if i in dda and i in ddb:
                    if dda[i]>ddb[i]:
                        for l in range(dda[i]-ddb[i]):
                            rra.append(i)
                    elif ddb[i]>dda[i]:
                        for l in range(ddb[i]-dda[i]):
                            rrb.append(i)
                elif i in dda:
                    for k in range(dda[i]):
                        rra.append(i)
                elif i in ddb:
                    for k in range(ddb[i]):
                        rrb.append(i)
            minimum = min(a+b)
            rra.sort()
            rrb.sort(reverse = True)
            cost = 0
            for i in range(len(rra)):
                cost+=min(min(rra[i],rrb[i]), 2 * minimum )
            print(cost)