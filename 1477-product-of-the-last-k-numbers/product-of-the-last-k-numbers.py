class ProductOfNumbers:
 def __init__(s):s.p=[1]
 def add(s,x:int)->None:s.p=[1]if x<1 else s.p+[s.p[-1]*x]
 def getProduct(s,k:int)->int:return 0 if k>=len(s.p) else s.p[-1]//s.p[-k-1]