
#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def findCycleStart(self, head):
    #TODO Write your code here
    fast = head
    slow = head
    while True:
      fast = fast.next.next
      slow = slow.next
      if fast == slow:
        break
    slow2 = head
    while slow2!=slow:
      slow = slow.next
      slow2 = slow2.next
    return slow2
