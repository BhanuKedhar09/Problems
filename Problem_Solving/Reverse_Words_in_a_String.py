#https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        stt = list(map(str, s.split(" ")))
        stt = stt[::-1]
        stt = " ".join(stt)
        stt = str(stt)
        return  " ".join(stt.split())