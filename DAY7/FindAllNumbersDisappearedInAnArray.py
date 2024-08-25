class Solution:
    def findDisappearedNumbers(self, nums):
        missing = []
        i = 0
        j = len(nums)
        while i<j:
            nxt = nums[i]-1
            if nxt<j and i!=(nums[i]-1):
                if nums[i]!=nums[nxt]:
                    nums[i], nums[nxt] = nums[nxt], nums[i]
                else:
                    i+=1
            else:
                i+=1
        # print(nums)
        for x in range(len(nums)):
            if x!=nums[x]-1:
                missing.append(x+1)
        return missing
                