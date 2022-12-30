#https://leetcode.com/problems/repeated-dna-sequences/description/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = dict()
        last_list = []
        for i in range(len(s)):
            # print(i,i+10, len(s))
            if i+10 <= len(s):
                # print("here")
                x = d.get(s[i:i+10])
                if x is None:
                    d[s[i:i+10]]= 1
                else:
                    d[s[i:i+10]] = d[s[i:i+10]] + 1
            else:
                break
        print(d)
        for dna, val in d.items():
            if val>1:
                last_list.append(dna)
        print(last_list)
        return last_list