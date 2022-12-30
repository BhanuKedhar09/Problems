#https://practice.geeksforgeeks.org/problems/triangle-pattern-1661493231/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_8

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N, 0, -1):
            for j in range(1, (N-i)+1):
                print(end = " ")
            for k in range((i*2) -1):
                print("*", end = "")
            print()
            