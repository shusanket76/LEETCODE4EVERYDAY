class Solution:
    def sortStack(self,stack):
        tempStack = []
        mainstack = []
        # ToDo: Write Your Code Here.
        l = 0
        while l<len(stack):
            if len(mainstack)==0:
                mainstack.append(stack[l])
                l+=1
            else:
                while mainstack and mainstack[-1]>stack[l]:
                    ele = mainstack.pop()
                    tempStack.append(ele)
                mainstack.append(stack[l])
                while tempStack:
                    el = tempStack.pop()
                    mainstack.append(el)
                l+=1
            

        return mainstack
