class Solution:
 def minimizeSum(self,n:List[int])->int:
  n.sort()
  return min(n[-1]-n[2],n[-2]-n[1],n[-3]-n[0])