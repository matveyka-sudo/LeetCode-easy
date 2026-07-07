from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sp=[]
        for index, number in enumerate(nums):
            if index > 0:
                if nums[index-1] + nums[index] == target:
                    sp.append(index-1)
                    sp.append(index)
            else:
                continue
        return sp