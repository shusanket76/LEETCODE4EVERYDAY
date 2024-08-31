class Solution:
  def findLength(self, str1, k):
      print(str1)
      max_length = 0
      # TODO: Write your code here
      l = 0
      r = 0
      hasmap = {}
      # print(str1)
      res = [0]
      haset = set()
      while r<len(str1):
        # print(haset)
        haset.add(str1[r])
        hasmap[str1[r]] = hasmap.get(str1[r], 0)+1
        while l<=r and len(haset)>k:
            hasmap[str1[l]] = hasmap.get(str1[l], 0)-1
            if hasmap[str1[l]]==0:
              haset.remove(str1[l])
            l+=1
        
        res[0] = max(res[0], r-l+1)
        r+=1
        
      return (res[0])