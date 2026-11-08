class Solution:
 def countServers(self,g:List[List[int]])->int:
  r=[sum(x)for x in g]
  c=[sum(x)for x in zip(*g)]
  return sum(g[i][j]and(r[i]>1 or c[j]>1)for i in range(len(g))for j in range(len(g[0])))