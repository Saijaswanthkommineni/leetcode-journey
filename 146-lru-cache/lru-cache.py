class Node:
 def __init__(self,k=0,v=0):
  self.k,self.v=k,v;self.p=self.n=None
class LRUCache:
 def __init__(self,c:int):
  self.c,self.s=c,0;self.d={};self.h,self.t=Node(),Node()
  self.h.n=self.t;self.t.p=self.h
 def get(self,k:int)->int:
  if k not in self.d:return -1
  n=self.d[k];self._rm(n);self._add(n);return n.v
 def put(self,k:int,v:int)->None:
  if k in self.d:
   n=self.d[k];self._rm(n);n.v=v;self._add(n)
  else:
   n=Node(k,v);self.d[k]=n;self._add(n);self.s+=1
   if self.s>self.c:
    l=self.t.p;self.d.pop(l.k);self._rm(l);self.s-=1
 def _rm(self,n:Node):
  n.p.n,n.n.p=n.n,n.p
 def _add(self,n:Node):
  n.n=self.h.n;n.p=self.h;self.h.n.p=n;self.h.n=n