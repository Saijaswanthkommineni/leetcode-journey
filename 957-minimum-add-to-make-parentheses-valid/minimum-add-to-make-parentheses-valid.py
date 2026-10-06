class Solution:
 def minAddToMakeValid(self,s:str)->int:
  st=[]
  for c in s:
   if c==')'and st and st[-1]=='(':st.pop()
   else:st.append(c)
  return len(st)