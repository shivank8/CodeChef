t = int(input())
for _ in range(t):
    coins = 0
    s = input()
    a, b = s.split()
    a = int(a)
    b = int(b)
    coins = a // b
    bal=a%b
    if(bal!=0):
        if(bal%2==0):
            coins+=1
        else:
            if(bal==1):
                coins+=1
            else:
                coins+=2
    print(coins)

