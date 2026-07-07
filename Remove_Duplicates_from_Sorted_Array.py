from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=len(nums)
        for i in nums:
            for y in nums:
                if i==y:
                    nums.remove(y)
                    k-=1
            if i not in nums:
                nums.append(i)
                k+=1
            else:
                continue
        return k