#https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718455/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_12

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N+1):
            for j in range(i):
                if ((i-j) % 2 ) == 0:
                    print("0", end = " ")
                else : 
                    print("1", end = " ")
            print()
            