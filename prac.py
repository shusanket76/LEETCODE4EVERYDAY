def findMissingNumber(nums):
    res = [x for x in range(len(nums)+1)]
    print(res)
    missing = 0
    for x in res:
      missing^=x
    for y in nums:
      missing^=y
    # TODO: Write your code here
    return missing
a = findMissingNumber([4, 0, 3, 1])
