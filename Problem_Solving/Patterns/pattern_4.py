#https://practice.geeksforgeeks.org/problems/triangle-number-1661428795/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_4

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N+1):
            for j in range(1,i+1):
                print(i, end = " ")
            print()
            