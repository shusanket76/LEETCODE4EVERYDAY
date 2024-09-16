class Solution:
    def dailyTemperatures(self, temperatures):
        # TODO: Write your code here
        res = [0 for x in range(len(temperatures))]
        stack = []
        l = 0
        while l<len(temperatures):
            if len(stack)==0:
                stack.append(l)
                l+=1
            else:
                # print(stack)
                while stack and temperatures[stack[-1]]<temperatures[l]:
                 
                    
                    pointer = stack.pop()
                    res[pointer] = l-pointer
                stack.append(l)
                l+=1

        return res
