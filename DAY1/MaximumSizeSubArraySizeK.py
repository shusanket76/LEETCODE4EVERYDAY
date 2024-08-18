class Solution:
  def findMaxSumSubArray(self,k, arr):
    # TODO: Write your code here
    l = 0
    r = 0
    res = 0
    temp = 0
    while r<len(arr):
      temp+=arr[r]
      while r<len(arr) and (r-l+1)==k:
        res = max(res, temp)
        temp-=arr[l]
        l+=1
      r+=1
    return res
    
