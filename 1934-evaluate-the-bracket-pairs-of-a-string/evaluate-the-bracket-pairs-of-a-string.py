class Solution:
 def evaluate(self,s:str,kn:List[List[str]])->str:
  d={k:v for k,v in kn};i=0;n=len(s);res=[]
  while i<n:
   if s[i]=='(':
    j=s.find(')',i+1)
    k=s[i+1:j];res.append(d.get(k,'?'));i=j
   else:res.append(s[i])
   i+=1
  return ''.join(res)