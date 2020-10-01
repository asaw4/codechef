tc = int(input())

for ii in range(tc):

    n = int(input())
    ar = list(map(int,input().split()))

    tot,cnt = 0,0

    br = []
    cr = []

    for i in range(n):
        if(ar[i]%4==0):
            br.append(i)
            cr.append(0)
            cnt+=1
            continue
        if(ar[i]%2==0):
            br.append(i)
            cr.append(1)
            cnt+=1

    tot = (n*(n+1))//2

    for i in range(cnt):
        if(cr[i]==0):
            continue

        if(i==0):
            a=-1
        else:
            a=br[i-1]
        if(i==cnt-1):
            b=n
        else:
            b=br[i+1];

        tot-= (br[i]-a)*(b-br[i])

    print(tot)
        
