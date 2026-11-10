class Solution:
 def climbStairs(self,n:int,c:List[int])->int:
  d=[0]+[10**18]*n
  for i in range(1,n+1):
   d[i]=min(d[j]+c[i-1]+(i-j)*(i-j)for j in range(max(0,i-3),i))
  return d[n]