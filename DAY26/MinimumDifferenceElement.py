class Solution:
  def searchMinDiffElement(self, arr, key):
    # TODO: Write your code here
    l = 0
    r = len(arr)-1
    res = [float("inf"), -1]
    while l<=r:
      mid = int((l+r)/2)
      wehave =  (arr[mid] - key)
      # if res[0]>wehave:
      #   res = [wehave, mid]

      if wehave>0:
        r = mid-1
      else:
        l=mid+1
      if res[0]>abs(wehave):
        res = [abs(wehave), mid]
    return arr[res[1]]
