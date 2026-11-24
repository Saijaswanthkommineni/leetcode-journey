from functools import reduce
from math import gcd
def lcm(a, b):
    return a * b // gcd(a, b)
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        cur = 1
        for r in range(len(nums)):
            cur *= nums[r]
            s = reduce(lcm, nums[l:r + 1]) * reduce(gcd, nums[l:r + 1])
            if cur == s:
                ans = max(ans, r - l + 1)
            while cur > s and l < r:
                cur //= nums[l]
                l += 1
        return ans