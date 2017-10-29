import numpy as np
alpha=np.zeros((1005,105,105))
beta=np.zeros((1005,105,105))
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
            for k in range(l,r):
                alpha[x][l][r]+=(p*alpha[y][l][k]*alpha[z][k+1][r]);

beta[root][0][n-1]=1
for len in range(n,0,-1):
    for i in range(n):
        l=i
        r=len+i-1
        if (r>n): break
        for j in range(cnt):
            (x,y,z,p)=mp[j]
            for o in range(cnt):
                (x2,y2,z2,p2)=mp[o]
                if (y2==z and z2==y and x2==x):
                    for k in range(l):
                        beta[z][l][r]+=(p*alpha[y][k][l-1]*beta[x][k][r])
                    for k in range(r+1,n):
                        beta[z][l][r]+=(p2*alpha[y][r+1][k]*beta[x][l][k])

for i in range(1,3):
    for j in range(n):
        for k in range(j,n):
            print(j,k,i,alpha[i][j][k])
print("-----------------------")
for i in range(1,3):
    for j in range(n):
        for k in range(j,n):
            print(j,k,i,beta[i][j][k])



print()
