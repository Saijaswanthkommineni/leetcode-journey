class BIT:
 def __init__(self,n):
  self.n=n;self.t=[0]*(n+1)
 def add(self,i,v):
  while i<=self.n:self.t[i]+=v;i+=i&-i
 def qry(self,i):
  s=0
  while i:s+=self.t[i];i-=i&-i
  return s
 def kth(self,k):
  i=s=0;b=1<<(self.n.bit_length()-1)
  while b:
   j=i+b
   if j<=self.n and s+self.t[j]<k:i=j;s+=self.t[j]
   b//=2
  return i+1

class Solution:
 def minOperations(self,nums:List[int],m:int,k:int)->int:
  from bisect import bisect_left
  INF=10**18;n=len(nums);c=[0]*n
  a=sorted(set(nums));z=len(a)
  f,s=BIT(z),BIT(z)
  def add(x,d):
   i=bisect_left(a,x)+1
   f.add(i,d);s.add(i,x*d)
  def cost():
   i=f.kth((m+1)//2);v=a[i-1]
   lc=f.qry(i);ls=s.qry(i)
   ts=s.qry(z)
   rc=m-lc;rs=ts-ls
   return v*lc-ls+rs-v*rc
  for i in range(m):add(nums[i],1)
  c[m-1]=cost()
  for i in range(m,n):
   add(nums[i-m],-1);add(nums[i],1)
   c[i]=cost()
  dp=[0]*(n+1)
  for t in range(1,k+1):
   nd=[INF]*(n+1)
   for i in range(t*m,n+1):
    nd[i]=min(nd[i-1],dp[i-m]+c[i-1])
   dp=nd
  return dp[n]