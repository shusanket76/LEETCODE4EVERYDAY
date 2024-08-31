class Solution:
  def findNumbers(self, nums):
    missingNumbers = []
    i = 0 
    j = len(nums)
    while i<j:
      n = nums[i]-1
      if nums[i]!=nums[n]:
        nums[i], nums[n] = nums[n], nums[i]
      else:
        i+=1
    print(nums)
    for i in range(len(nums)):
      if (i+1)!=nums[i]:
        missingNumbers.append(i+1)
      

    # TODO: Write your code here
    return missingNumbers
