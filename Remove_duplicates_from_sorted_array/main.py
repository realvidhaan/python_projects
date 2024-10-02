class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        c = 1
        while c < len(nums):
            if nums[c] != nums[c-1]:
                nums[p] = nums[c]
                p += 1
                c += 1
            else:
                c += 1
            
        return p