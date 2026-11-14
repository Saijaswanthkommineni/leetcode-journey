class Solution:
 def minimumSumSubarray(self,a:List[int],l:int,r:int)->int:
  ans=10**18;n=len(a)
  for k in range(l,r+1):
   s=sum(a[:k]);ans=min(ans,s)if s>0 else ans
   for i in range(k,n):
    s+=a[i]-a[i-k]
    if s>0:ans=min(ans,s)
  return[-1,ans][ans<10**18]