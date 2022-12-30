#https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        lena = len(nums1) +len(nums2)
        nums3 = nums1+nums2
        nums3.sort()
        half = (lena//2)-1
        if (lena % 2 ==0):
            median = (nums3[half]+nums3[half+1])/2
            print(nums3[half],nums3[half+1])
        else:
            median = nums3[lena//2]
        print(nums3,half,lena)
        return median