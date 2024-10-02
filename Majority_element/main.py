class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        maj_element = n//2
        elem = nums[maj_element]
        return elem