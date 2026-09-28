class Solution:
    def maxDepth(self,s:str)->int:
        dp=0
        mx=0
        for ch in s:
            if ch=='(':
                dp+=1
                mx=max(mx,dp)
            elif ch==')':
                dp-=1
        return mx