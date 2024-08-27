class Solution:
  def searchCeilingOfANumber(self, arr, key):
    # TODO: Write your code here
    l = 0
    found = False
    r = len(arr)-1
    while l<=r:
      mid = int((l+r)/2)
      if arr[mid]<key:
        l=mid+1
      else:
        found = True
        r=mid-1
    if found:
      return l
    return -1