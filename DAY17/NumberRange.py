class Solution:
  def findRange(self, arr, key):
    result = [- 1, -1]
    # TODO: Write your code here
    l = 0
    found = False 
    r = len(arr)-1
    while l<=r:
      mid = int((l+r)/2)
      if arr[mid]>key:
        r = mid-1
      elif arr[mid]<key:
        l=mid+1
      else:
        found = True
        break
    if found:
      l = r = mid
      while l>=0 and arr[l]==key:
        result[0] = l
        l-=1
      while r<len(arr) and arr[r] == key:
        result[1] = r
        r+=1
    print(result)
    return result
