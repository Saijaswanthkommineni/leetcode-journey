class Solution:
 def countDaysTogether(self,aA:str,lA:str,aB:str,lB:str)->int:
  d=(31,28,31,30,31,30,31,31,30,31,30,31)
  g=lambda x:sum(d[:int(x[:2])-1])+int(x[3:])
  return max(g(min(lA,lB))-g(max(aA,aB))+1,0)