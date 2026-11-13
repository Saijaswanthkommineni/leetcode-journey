class Solution:
 def countNonDecreasingSubarrays(self,a:List[int],k:int)->int:
  from collections import deque
  q=deque();c=r=0;j=len(a)-1
  for i,x in reversed(list(enumerate(a))):
   while q and a[q[-1]]<x:
    l=q.pop();c+=((q[-1] if q else j+1)-l)*(x-a[l])
   q.append(i)
   while c>k:
    c-=a[q[0]]-a[j]
    if q[0]==j:q.popleft()
    j-=1
   r+=j-i+1
  return r