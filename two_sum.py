class Solution(object):
    def twoNum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[int]
        """
        search_list = dict((v, i) for i, v in enumerate(nums))
        for k in range(len(nums)):
            if (target - nums[k] in search_list) and \
                    (k != search_list[target - nums[k]]):
                return [k, search_list[target - nums[k]]]


sol = Solution()
print sol.twoNum([2, 7, 11, 5], 9)
