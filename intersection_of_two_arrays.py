class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if nums1 == [] or nums2 == []:
            return []
        for x in nums1:
            if x in nums2:
                if x not in res:
                    res.append(x)
        return res
        # nums1=set(nums1)
        # nums2=set(nums2)
        # return list(nums1&nums2)


s = Solution()
print s.intersection([1], [1])
