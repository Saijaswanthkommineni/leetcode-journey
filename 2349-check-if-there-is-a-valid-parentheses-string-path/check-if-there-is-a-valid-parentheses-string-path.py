class Solution:
    def hasValidPath(self,g:list[list[str]])->bool:
        m,n=len(g),len(g[0])
        if (m+n-1)%2 or g[0][0]==')' or g[-1][-1]=='(':return False
        from functools import cache
        @cache
        def f(r,c,b):
            b+=1 if g[r][c]=='(' else -1
            if b<0 or b>(m-1-r)+(n-1-c):return False
            if r==m-1 and c==n-1:return b==0
            return r+1<m and f(r+1,c,b) or c+1<n and f(r,c+1,b)
        return f(0,0,0)