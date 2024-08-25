class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i,j = 0, len(nums)
        while i<j:
            nxt = nums[i]-1
            if nxt<len(nums) and i!=(nums[i]-1):
                if nums[i]!=nums[nxt]:
                    nums[i], nums[nxt] = nums[nxt], nums[i]
                else:
                    i+=1
            else:
                i+=1
        for x in range(len(nums)):
            if x!=nums[x]-1:
                return nums[x]


            
        