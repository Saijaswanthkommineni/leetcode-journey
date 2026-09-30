class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        dep=max_dep=0
        for c in seq:
            if c=="(":
                dep+=1
                max_dep=max(max_dep,dep)
            else:
                dep-=1
        half=max_dep//2
        res_dep=0
        res=[]
        for c in seq:
            if c=="(":
                res_dep+=1
            res.append(1 if res_dep>half else 0)
            if c==")":
                res_dep-=1
        return res