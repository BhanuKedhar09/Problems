#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if "--" in i:
                x= x-1
            elif "++" in i:
                x = x+1
            else:
                pass
        return x