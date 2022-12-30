#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s_l = list(set(list(s)))
        le = 0
        count_list = []
        count = 0
        oss= set()
        if not s:
            return 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if s[j] not in oss:
        #             oss.add(s[j])
        #             l = j-i+1
        #             le = max(le, l)
        #         elif j!=i :
        #             oss.remove(s[j])
        #             break
        #         else:
        #             pass
        #         print(oss, le)
            
        # return le

        #O(n^2)
        # s1 = ""
        # le =0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         if s[j] not in oss:
        #             oss.add(s[j])
        #             l = len(oss)
        #             le = max(l, le)
        #         else:
        #             oss.clear()
        #             break
        # return le

        #O(n)
        oss = set()
        res = 0
        l=0
        for i in range(len(s)):
            while s[i] in oss:
                oss.remove(s[l])
                l = l+1
            oss.add(s[i])
            res = max(res, i-l+1)
        return res




            


