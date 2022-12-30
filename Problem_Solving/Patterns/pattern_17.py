#https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285911/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_17

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N+1):
            for j in range((N-i)):
                print(end = " ")
            for k in range(65, 65+i):
                print(chr(k), end ="")
            for k in range(64+(i-1), 64, -1):
                print(chr(k), end = "")
            print()
