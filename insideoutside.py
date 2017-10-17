import numpy as np
alpha=np.zeros((1005,105,105))
mp={}


n=int(input())
cnt=-1
for i in range(n):
    cnt=cnt+1
    x,y,z=input().split()
    mp[cnt]=(int(x),int(y),int(z),0.1)


n,n_ter=input().split()
n=int(n)
n_ter=int(n_ter)
for i in range(n):
    x=input().split()
    for j in range(n_ter):
        cnt=cnt+1
        mp[cnt]=(int(x[0]),int(x[j+1]),0,0.1)


n=int(input())
a=input().split()
root=int(input())
for i in range(n):
    for j in range(cnt):
        (x,y,z,p)=mp[j]
        if (z==0 and y==int(a[i])) :
            alpha[x][i][i]=p

for len in range(2,n+1):
    for i in range(n):
        l=i
        r=len+i-1
        if (r>n): break
        for j in range(cnt):
            (x,y,z,p)=mp[j]
            for k in range(l,r+1):
                alpha[x][l][r]+=(p*alpha[y][l][k]*alpha[z][k+1][r]);

for i in range(1,3):
    for j in range(n):
        for k in range(j,n):
            print(j,k,i,alpha[i][j][k])

print()
