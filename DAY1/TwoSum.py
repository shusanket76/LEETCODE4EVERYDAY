class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        for x in range(len(nums)):
            weneed = target - nums[x]
            if weneed in hasmap:
                return [x, hasmap[weneed]]
            else:
                hasmap[nums[x]] = x
        
        