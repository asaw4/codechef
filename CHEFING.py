tc = input()
for ii in range(tc):
    n = input()
    ar = []
    for i in range(n):
        ar.append(raw_input())
    lr,mr=[0]*26,[0]*26
    for i in range(n):
        for j in range(len(ar[i])):
            x = ord(ar[i][j])-97
            if mr[x]==0:
                mr[x]+=1
                lr[x]+=1
            else:
                continue
        mr=[0]*26
    c = 0
    for i in range(26):
        if lr[i]==n:
            c+=1
    print c
