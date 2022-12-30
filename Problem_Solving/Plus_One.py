#https://leetcode.com/problems/plus-one/description/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nu = [str(i) for i in digits]
        num = ''.join(nu)
        num = int(num) + 1
        num = str(num) 
        re = [int(x) for x in num]
        return re