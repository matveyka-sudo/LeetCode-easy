from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.remove(val)
        if val in nums:
            self.removeElement(nums, val)
        return len(nums)