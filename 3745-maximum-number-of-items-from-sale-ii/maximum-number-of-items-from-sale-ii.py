class Solution:
 def maximumSaleItems(self,items:List[List[int]],budget:int)->int:
  from functools import cache
  from heapq import heapify,heappop
  f,p=zip(*items)
  h=[0]*(len(items)+1)
  for x in f:h[x]+=1
  @cache
  def d(x):return sum(h[x::x])-1
  mn=min(p)
  q=[(pr,fa)for fa,pr in items if pr<2*mn]
  heapify(q);ans=0
  while q and q[0][0]<=budget:
   pr,fa=heappop(q)
   c=min(d(fa),budget//pr)
   ans+=2*c;budget-=c*pr
  return ans+budget//mn