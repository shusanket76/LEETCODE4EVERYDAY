# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for x in range(n)] for y in range(m)]
        # print(matrix)
        top, left = 0,0
        bottom,right = len(matrix)-1, len(matrix[0])-1
        while top<=bottom:

            # top row
            for x in range(left, right+1):
                print("top row")
                print(top,x)
                if head is None:
                    return matrix
                matrix[top][x] = head.val
                head=head.next
            for x in range(top+1, bottom+1):
                print("right col")
                print(x,right)
                if head is None:
                    return matrix
                matrix[x][right] = head.val
                head = head.next
            for x in range(right-1, left-1, -1):
                print("down row")
                print(bottom,x)
                if head is None:
                    return matrix
                matrix[bottom][x] = head.val
                head = head.next
            for x in range(bottom-1, top, -1):
                print("left col")
                print(x,left)
                if head is None:
                    return matrix
                matrix[x][left] = head.val
                head = head.next
            top+=1
            left+=1
            bottom-=1
            right-=1
        # return (matrix if len(matrix)>1 else  [[head.val]])
        return (matrix)