#https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        open_brac = ["(", "{", "[" ]
        closed_brac = [")", "}", "]"]
        stack = []
        print(len(s))
        for i in s :
            if i in open_brac :
                stack.append(i)
            elif i in closed_brac :
                p  = closed_brac.index(i)
                if ((len(stack) > 0) and (open_brac[p] == stack[len(stack)-1])) :
                    stack.pop()
                else :
                    return 0
        if len(stack) == 0 :
            return 1
        else :
            return 0
            