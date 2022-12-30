#https://leetcode.com/problems/palindrome-number/description/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        num = str(num)
        num = num[::-1]
        print(num)
        if (num == str(x)):
            return 1
        return 0
        