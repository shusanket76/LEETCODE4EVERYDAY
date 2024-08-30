class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = []
        rightsum = []
        total = 0
        for x in range(len(nums)):
            if x==0:
                leftsum.append(0)
            else:
                total+=nums[x-1]
                leftsum.append(total)
        total+=nums[-1]

        # total2= total
        print(total)
        for y in range(len(nums)):
            if y==len(nums)-1:
                rightsum.append(0)
            else:
                total-=nums[y]

                rightsum.append(total)
            
        print(f"leftsum=>{leftsum}")
        print(f"rightsum=>{rightsum}")
        res = []
        # print(leftsum)
        # print(rightsum)
        for z in range(len(nums)):
            val = abs(leftsum[z]-rightsum[z])
            res.append(val)
            # prin/t(res)
            # print(1)
        return (res)