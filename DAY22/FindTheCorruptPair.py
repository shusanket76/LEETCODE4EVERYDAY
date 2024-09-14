class Solution:
  def findNumbers(self, nums):
    # TODO: Write your code here
    res = []
    l = 0
    while l<len(nums):
      currval = nums[l]
      if currval-1==l or currval==nums[currval-1]:
        l+=1
      else:
        temp = nums[currval-1]
        nums[currval-1] = currval
        nums[l] = temp
    for x in range(len(nums)):
      if x!=nums[x]-1:
        res.append(nums[x])
        res.append(x+1)

    return res
