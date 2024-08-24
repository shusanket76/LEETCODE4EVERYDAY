import math

class Solution:
  def findMinSubArray(self, s, arr):
    # TODO: Write your code here
    l = 0
    r = 0
    res = float("inf")
    tempsum = 0
    while r<len(arr):
      tempsum+=arr[r]

      while tempsum>=s:
        res = min(res, r-l+1)
        tempsum-=arr[l]
        l+=1
      r+=1
    if res==float("inf"):
      return 0 
    return res       
