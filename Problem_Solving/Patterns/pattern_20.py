#https://practice.geeksforgeeks.org/problems/double-triangle-pattern-1662287416/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_20

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N+1):
            for j in range(1,i+1):
                print("*", end = "")
            for j in range((N+N) - (i+i)):
                print(end = " ")
            for j in range(1,i+1):
                print("*", end = "")
            print()
        for i in range(N-1, 0, -1):
            for j in range(i,0,-1):
                print("*", end = "")
            for j in range(((N+N)-(i+i)), 0, -1):
                print(end = " ")
            for j in range(i,0,-1):
                print("*", end = "")
            print()
