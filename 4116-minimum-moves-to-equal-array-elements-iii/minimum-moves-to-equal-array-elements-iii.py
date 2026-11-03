class Solution:
 def minMoves(self,n:List[int])->int:
  return max(n)*len(n)-sum(n)