t = int(input())

for i in range(t):

    n, x = map(int, input().split())

    a = [int(a) for a in input().split()]

    Lst = []

    k = 0

    ans = 0

    if len(set(a)) == 1:

        k = a[0]

        c = 1

        while (True):

            if x < k:
                x = x * 2

                c += 1

            if x >= k:
                break

        ans = c + len(a) - 1

    else:

        a.sort()

        Lst = []

        for j in a:

            if j >= x:
                Lst.append(j)

        if len(a) == len(Lst):

            j = 0

            c = 0

            d = 0

            if a[0] == x:

                c = 0

            else:

                c = 1

            while (True):

                if j == len(a):

                    break

                elif a[j] < x:

                    for k in range(j + 1, len(a) - 1):

                        if k < a[j] * 2:
                            d = 1

                            break

                    if d == 1:

                        x = a[j] * 2

                        c += 1

                        j += 1

                    else:

                        c += 1

                        j += 1

                elif a[j] == x:

                    x = a[j] * 2

                    j += 1

                    c += 1

                elif a[j] > x:

                    while (True):

                        if x < a[j]:
                            x = x * 2

                            c += 1

                        if x >= a[j]:
                            x = a[j]

                            j += 1

                            break

            ans = c

        elif len(Lst) == 0:

            ans = len(a)



        elif len(Lst) != 0 and len(Lst) != a:

            d = 0

            j = 0

            c = 0

            j = 0

            while (True):

                if j == len(a):

                    break

                elif a[j] < x:

                    for k in range(j + 1, len(a)):

                        if a[k] <= a[j] * 2:
                            d = 1

                            break

                    if d == 1:

                        x = a[j] * 2

                        c += 1

                        j += 1

                    elif d == 0:

                        x = x * 2

                        c += 1

                        j += 1

                elif a[j] == x:

                    x = a[j] * 2

                    c += 1

                    j += 1

                elif a[j] > x:

                    while (True):

                        if x < a[j]:
                            x = x * 2

                            c += 1

                        if x >= a[j]:
                            x = a[j]

                            j += 1

                            break
            ans = c

    print(ans)

