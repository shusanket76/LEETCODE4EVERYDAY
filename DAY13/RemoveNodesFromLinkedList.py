# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            # print(stack)
            # print("----------------------------------------------------------")
            while stack and stack[-1].val<curr.val:
                print(True)
                # print(f"stack=>{stack}, curr=>{curr}")
                # print("----------------------------------------------------------")
                stack.pop()
            if stack:
                stack[-1].next = curr
                # print(f"final=>{stack}")
            stack.append(curr)
            curr = curr.next
        return stack[0]
        