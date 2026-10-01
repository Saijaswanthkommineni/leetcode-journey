class Solution:
    def isValid(self,s:str)->bool:
        sk=[]
        mp={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for ch in s:
            if ch in "({[":
                sk.append(ch)
            else:
                if not sk or sk.pop()!=mp[ch]:
                    return False
        return len(sk)==0