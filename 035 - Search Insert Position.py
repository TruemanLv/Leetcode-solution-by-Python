# Solution_1 39ms
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """   
        return (len([x for x in nums if x<target]))

# Solution_2 46ms

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        pos = 0
        while first <= last:
                mid = (first + last) / 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    first = mid + 1
                    pos = mid + 1
                else:
                    last = mid - 1
                    pos = mid
        return pos

# Solution_3  32ms

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        while first < last:
                mid = (first + last + 1) / 2
                if nums[mid] == target:
                      return mid
                if nums[mid] < target:
                      first = mid + 1
                else:
                      last = mid - 1
        if nums[last] < target:
                return last + 1
        if target <= nums[last]:
                return last
        if target < nums[first]:
                return first
        return first + 1