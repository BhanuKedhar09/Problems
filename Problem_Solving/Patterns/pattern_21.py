#https://practice.geeksforgeeks.org/problems/square-pattern-1662287714/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_21

class Solution:
    def printTriangle(self, N):
        # Code here
        print("*"*N)
        for i in range(1,N-1):
            print("*", end = "")
            print(' '*(N-2), end = "")
            print("*")
            # print("*",''*(N-2), "*")
        print("*"*N)