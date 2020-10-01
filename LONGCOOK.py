ar = [0]*400
br = [0]*400
day = 3
ans = 0
for i in range(1,401):
    if(i%4==0 and i%100!=0):
        if(day==5):
            ans+=1
            br[i-1]=1
        day = (day+2)%7
    else:
        if(day>=5):
            ans+=1
            br[i-1]=1
        day = (day+1)%7
    ar[i-1]=ans
            
tc = int(input())
for ii in range(tc):
    ans = 0
    m1,y1 = map(int, input().split())
    m2,y2 = map(int, input().split())
    ans1 = (y2//400)*101
    if(y2%400!=0):
        ans1 += ar[(y2%400)-1]
    ans2 = ((y1-1)//400)*101
    if((y1-1)%400!=0):
        ans2 += ar[((y1-1)%400)-1]
    ans = ans1-ans2
    if(m1>2 and br[(y1%400)-1]==1):
        ans-=1
    if(m2<2 and br[(y2%400)-1]==1):
        ans-=1
    print(ans)
