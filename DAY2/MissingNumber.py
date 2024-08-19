class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i,n=0, len(nums)
        while i<n:
            j = nums[i]
            if nums[i]<n and nums[i]!=nums[j]:
                nums[i], nums[j]=nums[j], nums[i]
            else:
                i+=1
        for x in range(len(nums)):
            if nums[x]!=x:
                return x
        return n
