class Solution:
 def numOfSubarrays(self,a:List[int])->int:
  m=10**9+7;x=y=r=0
  for v in a:
   x,y=(y,x+1)if v&1 else(x+1,y)
   r=(r+y)%m
  return r