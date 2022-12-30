#https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        if not nums:
            return 0
        for i in range(0,len(nums)):
            if nums[i] == val :
                nums[i] = 100
            else:
                count +=1
        nums.sort()
        return count

