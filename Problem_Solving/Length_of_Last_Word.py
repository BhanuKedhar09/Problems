#https://leetcode.com/problems/length-of-last-word/description/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss = list(map(str, s.strip().lstrip().split(' ')))
        lena = len(ss)
        last_str = str(ss[lena-1])
        return len(last_str)