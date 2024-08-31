# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        count = 0
        po = dummy
        first = dummy
        end = None
        nxt = None
        while count<left or count<right:
            if count+1==left:
                middle = first.next
                first.next = None
                prev,curr = None, middle
                while curr:

                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                    if count+1==right:
                        if nxt:
                            end = nxt
                        else:
                            end = None
                        count+=1
                        break
                        # pass
                    count+=1
            else:
                first = first.next
                count+=1
        res = po
        res1 = res
        while res and res.next:
            res = res.next
        if prev:
            res.next = prev
            while res and res.next:
                res = res.next
        if end:
            res.next = end
            # print(res1)
            # return
        return (res1.next)
                

