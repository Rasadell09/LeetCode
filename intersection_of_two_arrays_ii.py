class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        C = collections.Counter
        return list((C(nums1) & C(nums2)).elements())


s = Solution()
print s.intersection([1, 2, 2, 1, 4, 4, 1, 2], [1, 2, 4, 1, 2, 6, 7])
