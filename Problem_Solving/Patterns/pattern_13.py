#https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718712/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_13

class Solution:
    def printTriangle(self, N):
        # Code here
        t = 1
        for i in range(1, N+1):
            for j in range(1, i+1):
                print(t, end = " ")
                t = t+1
            print()