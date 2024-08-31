#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end


class Solution:
  def merge(self, intervals_a, intervals_b):
    result = []
    l = 0
    r = 0
    while l<len(intervals_a) and r<len(intervals_b):
      print(l,r)
      if intervals_a[l].end<intervals_b[r].start:
        l+=1
      elif intervals_a[l].start>intervals_b[r].end:
        r+=1
      elif intervals_a[l].end>=intervals_b[r].end:
        x1 = max(intervals_b[r].start, intervals_a[l].start)
        y1 = min(intervals_b[r].end,intervals_a[l].end)
        result.append([x1,y1])
        r+=1
      elif intervals_a[l].end<intervals_b[r].end:
        x1 = max(intervals_b[r].start, intervals_a[l].start)
        y1 = min(intervals_b[r].end,intervals_a[l].end)
        result.append([x1,y1])
        l+=1
    # TODO: Write your code here
    return (result)
