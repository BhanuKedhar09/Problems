#https://practice.geeksforgeeks.org/problems/double-triangle-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_19


class Solution:
    def printTriangle(self, N):
        # Code here
        # for i in range(N+N, 0 , -1):
        #     # for j in range(N+1, i, -1):
        #     #     print("*", end = "")
        #     # for k in range(N, 0, -1):
        #     #     for l in range(N-k):
        #     #         print(end = " ")
        #     #     for l in range(k, 0, -1):
        #     #         print("*", end = "")
        #     #     print()
        #     for j in range()
        for i in range(N,0,-1):
            for j in range(i,0,-1):
                print("*", end = "")
            for j in range(((N+N) - (i+i)), 0, -1):
                print(end = " ")
            for j in range(i,0,-1):
                print("*", end="")
            print()
        for i in range(1, N+1):
            for j in range(i):
                print("*", end = "")
            for j in range((N+N)-(i+i)):
                print(end =" ")
            for j in range(i):
                print("*", end = "")
            print()