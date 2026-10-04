class Solution:
 def checkValidString(self,s:str)->bool:
  n=len(s);dp=[[0]*n for _ in range(n)]
  for i,ch in enumerate(s):dp[i][i]=(ch=='*')
  for i in range(n-2,-1,-1):
   for j in range(i+1,n):
    dp[i][j]=(s[i]in'(*'and s[j]in'*)'and(i+1==j or dp[i+1][j-1]))or any(dp[i][k]and dp[k+1][j]for k in range(i,j))
  return dp[0][n-1]