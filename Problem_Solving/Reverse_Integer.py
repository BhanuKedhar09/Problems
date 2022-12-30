#https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        absol = str(abs(x))
        absol = absol[::-1]
        absol = int(absol)
        if absol >= 2147483651 :
            return 0
        rev=0
        num = x
        if (x<0):
            rev  = str(x)[::-1]
            rev1 = len(str(x))
            x = str(x)
            rev2 = rev[0:rev1-1]
            stri ="-"
            rev3 = stri + rev2
            return int(rev3)
        else:
            while(num>0):
                remainder = num % 10
                rev = (rev * 10) + remainder
                num = num//10
            return rev
            
        
        