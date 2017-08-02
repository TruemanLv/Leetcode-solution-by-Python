class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        index = 0
        while index<len(nums):
             if nums[index]!=val:
                nums[count]=nums[index]
                count+=1
             index+=1
        return count 
