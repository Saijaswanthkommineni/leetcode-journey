class Solution:
 def minSumSquareDiff(self,nums1:List[int],nums2:List[int],k1:int,k2:int)->int:
  d=[abs(a-b)for a,b in zip(nums1,nums2)]
  k=k1+k2
  if sum(d)<=k:return 0
  M=max(d)
  def ok(t):return sum(max(x-t,0)for x in d)<=k
  l,r=0,M-1;T=M
  while l<=r:
   m=(l+r)//2
   if ok(m):T=m;r=m-1
   else:l=m+1
  for i,x in enumerate(d):
   u=max(0,x-T);d[i]=min(T,x);k-=u
  for i,x in enumerate(d):
   if not k:break
   if x==T:d[i]-=1;k-=1
  return sum(x*x for x in d)