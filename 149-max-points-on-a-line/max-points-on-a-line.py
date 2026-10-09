class Solution:
 def maxPoints(self,p:List[List[int]])->int:
  n=len(p);ans=1
  for i in range(n):
   x1,y1=p[i]
   for j in range(i+1,n):
    x2,y2=p[j];cnt=2
    for k in range(j+1,n):
     x3,y3=p[k]
     if (y2-y1)*(x3-x1)==(y3-y1)*(x2-x1):cnt+=1
    ans=max(ans,cnt)
  return ans