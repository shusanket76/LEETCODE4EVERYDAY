class Solution:
  def moveElements(self, arr):
    # TODO: Write your code here
    nextnonduplicate = 1
    i = 1
    while i<len(arr):
      if arr[nextnonduplicate-1]==arr[i]:
        i+=1
      else:
        arr[nextnonduplicate] = arr[i]
        i+=1
        nextnonduplicate+=1
    return nextnonduplicate