# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = "".join(ch for ch in s if ch.isalnum())
        c_rev = c[::-1]
        # print(c)
        # print(c_rev)
        if c.lower() == c_rev.lower():
            return True
        return False