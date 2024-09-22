class Solution:
  def canPartition(self, num):
    # TODO: Write your code here
    res = [float('inf')]

    def dfs(arr1, arr2, pointer):
      if pointer==len(num):
        diff = abs(arr1-arr2)
        if res[0]>diff:
          res[0] = diff
        return 
      
      arr1+=num[pointer]
      dfs(arr1, arr2, pointer+1)
      arr1-=num[pointer]
      arr2+=num[pointer]
      dfs(arr1, arr2, pointer+1)
    arr1=0
    arr2=0
    pointer=0
    dfs(arr1, arr2, pointer)
    return (res[0])
