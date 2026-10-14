class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num*9 : return ""
        res = ""
        while num:
            res += str(min(9, sum))
            sum -= 9
            if sum < 0 : sum = 0
            num -= 1
        return res
        