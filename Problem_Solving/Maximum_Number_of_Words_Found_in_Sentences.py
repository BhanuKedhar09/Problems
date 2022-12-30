# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0
        for i in sentences:
            le = len(i.split(" "))
            max_len = max(max_len, le)
        return max_len