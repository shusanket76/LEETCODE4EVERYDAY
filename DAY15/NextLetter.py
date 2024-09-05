class Solution:
  def searchNextLetter(self, letters, key):
    l = 0
    r = len(letters)-1
    while l<=r:
      mid = int((l+r)/2)
      if letters[mid]<=key:
        l = mid+1
      else:
        r = mid-1
    # TODO: Write your code here
    if l>=len(letters):
      return letters[0]
    return letters[l]
