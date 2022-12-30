#https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        size = len(strs)
        end = min(len(strs[0]), len(strs[size - 1]))
        i=0
        pre = ''
        while (i < end and strs[0][i] == strs[size-1][i]) :
            pre = pre + strs[0][i]
            i = i+1
        return pre
