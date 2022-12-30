#https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # print(n) 
        arr = []
        for i in range(numRows):
            arr.append([])
        

        if len(s) <= numRows or len(s) == 2 or numRows == 1:
            return s
        m = numRows
        middle_jumps = (m*2) -4
        jumps = (m*2)-2
        str_count = 0
        oss = ""
        for i in range(numRows):
            if i==0 or i==numRows-1:
                for j in range(i,len(s), jumps):
                    arr[i].append(s[j])
            else:
                for j in range(i,len(s), jumps):
                    arr[i].append(s[j])
                    # print("once")
                    if j+middle_jumps <= len(s)-1 :
                        # print(j+middle_jumps, len(s))
                        arr[i].append(s[j+middle_jumps])
                    # print(arr)
                middle_jumps = middle_jumps-2
                # print(arr)
                # middle_jumps = (m*2) -4
        print(arr)
        for li in arr:
            oss = oss + "".join(li)

        return oss