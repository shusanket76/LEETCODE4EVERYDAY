arr = [2, 3, 3, 3, 6, 9, 9]
def moveElements(arr):
    # TODO: Write your code here
    l = 0 
    r = 0
    while r<len(arr):
      if (r-1)>=0:
        if arr[r-1]==arr[r]:
          r+=1
        else:
          if l+1!=r:
            arr[l+1], arr[r] = arr[r], arr[l+1]
          l+=1
          r+=1
      else:
        r+=1
    print(arr)
    print(l)
    print(r)
a  = moveElements(arr)
