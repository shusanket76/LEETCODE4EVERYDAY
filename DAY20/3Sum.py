class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for x in range(len(nums)):
            if x>0 and nums[x]==nums[x-1]:
                continue
            l=x+1
            r = len(nums)-1
            while l<r:
                wehave = nums[x]+nums[l]+nums[r]
                if wehave<0:
                    l+=1
                elif wehave>0:
                    r-=1
                else:
                    res.append([nums[x], nums[l], nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                
        return res