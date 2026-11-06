class Solution:
 def countServers(self,n:int,logs:List[List[int]],x:int,q:List[int])->List[int]:
  from collections import Counter
  logs.sort(key=lambda p:p[1])
  c=Counter();ans=[0]*len(q);l=r=0
  for t,i in sorted((v,j)for j,v in enumerate(q)):
   while r<len(logs) and logs[r][1]<=t:
    c[logs[r][0]]+=1;r+=1
   while l<len(logs) and logs[l][1]<t-x:
    u=logs[l][0];c[u]-=1
    if not c[u]:del c[u]
    l+=1
   ans[i]=n-len(c)
  return ans