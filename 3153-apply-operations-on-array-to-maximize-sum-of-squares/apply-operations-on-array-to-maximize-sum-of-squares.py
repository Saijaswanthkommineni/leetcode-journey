class Solution:
 def maxSum(self,nums:List[int],k:int)->int:
  M=10**9+7;bc=[0]*31
  for x in nums:
   for i in range(31):
    if x>>i&1:bc[i]+=1
  ans=0
  for _ in range(k):
   cur=0
   for i in range(31):
    if bc[i]>0:cur|=1<<i;bc[i]-=1
   ans=(ans+cur*cur)%M
  return ans