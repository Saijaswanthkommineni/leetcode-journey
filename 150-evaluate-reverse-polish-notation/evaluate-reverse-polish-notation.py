class Solution:
 def evalRPN(self,t:List[str])->int:
  import operator as o
  op={'+':o.add,'-':o.sub,'*':o.mul,'/':o.truediv}
  st=[]
  for x in t:
   if x in op:
    b,a=st.pop(),st.pop()
    st.append(int(op[x](a,b)))
   else:st.append(int(x))
  return st[0]