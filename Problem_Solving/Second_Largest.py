#https://practice.geeksforgeeks.org/problems/second-largest3735/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=second-largest

class Solution:

	def print2largest(self,arr, n):
		# code here
		maximum = 1000000
        # mimi = arr[0]
        second_maxi = 0
        # second_mimi = mimi
        for i in arr:
            if maximum < i or second_maxi :
                # print(i)
                second_maxi = maximum
                maximum = i
            elif second_maxi < i and second_maxi != maximum:
                second_maxi = i
            else : pass
        return second_maxi