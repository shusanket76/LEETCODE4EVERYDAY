class Solution:
  def searchTriplets(self, arr, target):
    res = [0]
    arr.sort()
    print(arr)
    for x in range(len(arr)):

      l = x+1
      r = len(arr)-1
      while l<r:
        wehave = arr[x]+arr[l]+arr[r]
        if wehave>=target:
          r-=1
        else:
          res[0]+=r-l
          l+=1
    return res[0]
