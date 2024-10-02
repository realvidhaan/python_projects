class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m
        for element in nums2:
            nums1[i] = element
            i += 1
        return nums1.sort()