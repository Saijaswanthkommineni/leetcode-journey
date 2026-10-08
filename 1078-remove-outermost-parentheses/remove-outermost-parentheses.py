class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r=[]
        dh=0
        for ch in s:
            if ch=='(':
                if dh>0:
                    r.append(ch)
                dh+=1
            else:
                dh-=1
                if dh>0:
                    r.append(ch)
        return "".join(r)