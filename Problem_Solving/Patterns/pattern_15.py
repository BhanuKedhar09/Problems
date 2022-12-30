#https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285196/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_15

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N, 0, -1):
            for j in range(65, 65+i):
                print(chr(j), end = "")
            print()
            