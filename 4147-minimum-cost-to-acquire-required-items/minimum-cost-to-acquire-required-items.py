class Solution:
 def minimumCost(self,a:int,b:int,c:int,x:int,y:int)->int:
  m=min(x,y)
  return min(x*a+y*b,m*c+(x-m)*a+(y-m)*b,max(x,y)*c)