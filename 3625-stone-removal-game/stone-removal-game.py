class Solution:
 def canAliceWin(self,n:int)->bool:
  p=10;a=1
  while n>=p:
   n-=p;p-=1;a^=1
  return a<1