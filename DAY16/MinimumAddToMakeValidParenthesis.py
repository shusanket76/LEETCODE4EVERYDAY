class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        res = 0
        # ToDO: Write Your Code Here.
        for x in S:
            if x==")":
                if len(stack)!=0:
                    stack.pop()
                else:
                    res+=1
            else:
                stack.append("(")
        res+=len(stack)
        

        return res

