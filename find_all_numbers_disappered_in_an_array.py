class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
            print nums
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]



s = Solution()
print s.findDisappearedNumbers([4, 6, 5, 7, 6, 5, 3, 1])
