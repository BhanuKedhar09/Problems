#https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718013/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_10

class Solution:
    def printTriangle(self, N):
        # Code here
        m = N
        for i in range(1, N):
            for j in range(i):
                print("*", end = " ")
            print()
        for i in range(m, 0, -1):
            for j in range(i):
                print("*", end = " ")
            print()