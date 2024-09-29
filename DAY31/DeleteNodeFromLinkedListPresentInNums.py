# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0)
        tail = dummy
        tail.next = head
        while tail and tail.next:
            if tail.next.val in nums:
                tail.next = tail.next.next
            else:
                tail=tail.next
        return dummy.next
        