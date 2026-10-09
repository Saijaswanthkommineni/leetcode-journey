class Solution:
    def minInsertions(self, s: str) -> int:
        a=l=i=0
        n=len(s)
        while i<n:
            if s[i]=='(':l+=1
            else:
                if i<n-1 and s[i+1]==')':i+=1
                else:a+=1
                if l==0:a+=1
                else:l-=1
            i+=1
        return a+l*2