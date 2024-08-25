# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        maxvalue = 0
        dummy = ListNode()
        tail = dummy
        tail.next = prev
        while tail and tail.next:
            nextval = tail.next.val
            maxvalue = max(maxvalue, nextval)
            if maxvalue>nextval:
                tail.next = tail.next.next
            else:
                tail = tail.next
        prev1, curr1 = None, dummy.next
        while curr1:
            nxt1 = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = nxt1
        return (prev1)

        