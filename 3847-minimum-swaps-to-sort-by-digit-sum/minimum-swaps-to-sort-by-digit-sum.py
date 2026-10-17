class Solution:
 def minSwaps(self,nums:List[int])->int:
  def f(x):
   s=0;t=x
   while x:s+=x%10;x//=10
   return s,t
  a=sorted(nums,key=f)
  p={x:i for i,x in enumerate(nums)}
  ans=0
  for i in range(len(nums)):
   if a[i]!=nums[i]:
    x,y=p[a[i]],p[nums[i]]
    p[nums[i]],p[a[i]]=x,y
    nums[y],nums[x]=a[i],nums[i]
    ans+=1
  return ans