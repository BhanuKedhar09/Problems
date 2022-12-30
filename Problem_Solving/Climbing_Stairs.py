#https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        one_pos = 1
        two_pos = 1
        
        for i in range(n-1):
            temp = one_pos
            one_pos  = one_pos + two_pos
            two_pos = temp
        return one_pos
