def searchMinDiffElement(arr, key):
    # TODO: Write your code here
    l = 0
    r = len(arr)
    res = [float("inf"), -1]
    while l<=r:
      mid = int((l+r)/2)
      wehave =  (arr[mid] - key)


      if wehave>0:
        r = mid-1
      else:
        l=mid+1
      if res[0]>abs(wehave):
        res = [abs(wehave), mid]
    return arr[res[1]]
a = searchMinDiffElement([1,3,8,10,15], 12)