class Solution:
 def assignTasks(self,s:List[int],t:List[int])->List[int]:
  from heapq import heapify,heappop,heappush
  a=[(w,i)for i,w in enumerate(s)];heapify(a)
  b=[];res=[]
  for i,x in enumerate(t):
   while b and b[0][0]<=i:
    _,w,j=heappop(b)
    heappush(a,(w,j))
   if a:
    w,j=heappop(a)
    heappush(b,(i+x,w,j))
   else:
    tm,w,j=heappop(b)
    heappush(b,(tm+x,w,j))
   res.append(j)
  return res