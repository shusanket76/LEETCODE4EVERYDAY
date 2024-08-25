class Solution:
  def sort(self, nums):
    # TODO: Write your code here
    for x in range(len(nums)):
      while x+1!=nums[x]:
        idx1 = x
        idx2 = nums[idx1]
        idx2-=1
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
    

    return nums
