#https://practice.geeksforgeeks.org/problems/triangle-number-1661489840/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_6

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N, 0, -1):
            for j in range(1, i+1):
                print(j, end = " ")
            print()