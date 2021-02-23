class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums2.sort()
        for num in nums1:
            # 이진 검색 bisect
            i2 = bisect.bisect_left(nums2,num)
            if len(nums2)>0 and len(nums2)>i2 and nums2[i2] == num:
                res.append(num)
        return set(res)
