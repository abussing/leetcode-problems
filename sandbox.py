

from typing import Optional, List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ourdict = {}

        for i in range(len(nums)):

            desired = target - nums[i]

            if desired in ourdict:

                return [i, ourdict[desired]]
            
            else:

                ourdict[nums[i]] = i
            
        return list()
    
what = Solution().twoSum(nums=[-1,-2,-3,-4,-5], target=-8)


what

