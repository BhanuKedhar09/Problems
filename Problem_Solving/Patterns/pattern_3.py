#https://practice.geeksforgeeks.org/problems/triangle-number/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_3

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for i in range(1, i+1):
                print(i, end = " ")
            print()