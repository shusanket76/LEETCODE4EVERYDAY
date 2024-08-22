class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftsum=[]
        rightsum=[]
        summ = 0
        for x in nums:
            leftsum.append(summ)
            summ+=x
        summ= 0
        for y in nums[::-1]:
            rightsum.append(summ)
            summ+=y
        
        for x in range(len(leftsum)):
            if leftsum[x]==rightsum[len(rightsum)-x-1]:
                return x
        return -1