#https://practice.geeksforgeeks.org/problems/triangle-pattern-1662286302/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_18


class Solution:
    def printTriangle(self, N):
        # Code here
        k =N-1
        for i in range(1,N+1):
            k = 64+N
            for j in range(k, k-i, -1):
                print(chr(j), end = " ")
            print()
            