#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>
#define MAXN 1000
using namespace std;

struct pair3
{
	int from,to1,to2;	
	double p;
	bool operator<(const pair3& p)  const
	{
		return (from*100+to1*10+to2)<p.from*100+p.to1*10+p.to2;
	}
};
map<pair3,int> mp3;
map<int,pair3> mp3_t;
int cnt=0;
int a[MAXN],root;
void addedge(int from,int to1,int to2)
{
	cnt++;
	pair3 p3;
	p3.from=from;
	p3.to1=to1;
	p3.to2=to2;
	p3.p=0.1;
	mp3[p3]=cnt;
	mp3_t[cnt]=p3;
	return ;
}



double alpha[MAXN][105][105];
double beta[MAXN][105][105];

int main()
{
	freopen("testcase.txt","r",stdin);
	int n;
	cin>>n;
	int x,y,z;
	memset(alpha,0,sizeof(alpha));
	memset(beta,0,sizeof(beta));
	for (int i=1;i<=n;i++) 
	{
		cin>>x>>y>>z;
		x+=3;y+=3;z+=3;
		addedge(x,y,z);
	}
	int n_ter;
	cin>>n>>n_ter;
	for (int i=1;i<=n;i++)
	{
		cin>>x;
		x+=3;
		for (int j=1;j<=n_ter;j++) 
		{
			cin>>y;
			y+=3;
			addedge(x,y,0);
		}
	}
	cin>>n;
	for (int i=1;i<=n;i++) {cin>>a[i];a[i]+=3;}
	for (int i=1;i<=n;i++)
	{
		for (int j=1;j<=cnt;j++)
		{
			pair3 p3;
			p3=mp3_t[j];
			x=p3.from;
			y=p3.to1;
			z=p3.to2;
			if (z==0&&y==a[i]) alpha[x][i][i]=p3.p;
		}
	}
	for (int len=2;len<=n;len++)
	{
		for (int i=1;i<=n;i++)
		{
			int l=i,r=len+i-1;
			if (r>n) break;
			for (int j=1;j<=cnt;j++)
			{
				pair3 p3;
				p3=mp3_t[j];
				x=p3.from;
				y=p3.to1;
				z=p3.to2;
				for (int k=l;k<=r;k++)
					alpha[x][l][r]+=(p3.p*alpha[y][l][k]*alpha[z][k+1][r]);
			}
		}
	}
	cin>>root;
	beta[root][1][n]=1;
	for (int i=1;i<=2;i++)
	{
		for (int j=1;j<=n;j++)
		{
			for (int k=j;k<=n;k++)
			{
				printf("(%d, %d) %d %.5lf\n",j-1,k-1,i-3,alpha[i][j][k]);
			}
		}
	}
	// ans_cnt++;
	// ans[ans_cnt]=root;
	// search(root);
	return 0;
}








