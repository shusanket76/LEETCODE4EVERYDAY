#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

#  def print_interval(self):
#    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class Solution:
  def canAttendAllAppointments(self, intervals):
    # TODO: Write your code here
    intervals.sort(key=lambda x: x.start)
    l = 0
    lastend = float("-inf")
    while l<len(intervals):
      currelement = intervals[l]
      if lastend>currelement.start:
        return False
      l+=1
      lastend = currelement.end
    return True
