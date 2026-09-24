class Solution:
 def minOperations(self,nums:List[int],x:int)->int:
  tgt=sum(nums)-x;d={0:-1};s=0;mx=-1
  for i,v in enumerate(nums):
   s+=v
   if s not in d:d[s]=i
   if s-tgt in d:mx=max(mx,i-d[s-tgt])
  return -1 if mx==-1 else len(nums)-mx