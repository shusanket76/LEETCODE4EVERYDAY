def findRange(arr, key):
    result = [- 1, -1]
    # TODO: Write your code here
    l = 0 
    r = len(arr)-1
    while l<=r:
      mid = int((l+r)/2)
      if arr[mid]>=key:
        r = mid-1
      else:
        l=mid+1
    if arr[r]==key:
      result[0] =r 
      while r<len(arr) and arr[r]==key:
        result[1] = r 
        r+=1  
    print(result)
    return result

arr = [4, 6, 6, 6, 9]
key = 6
a = findRange(arr, key)