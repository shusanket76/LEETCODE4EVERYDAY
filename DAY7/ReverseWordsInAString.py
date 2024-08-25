class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        stack = []
        for x in s:
            if len(temp)==0 and x==" ":
                continue
            elif len(temp)!=0 and x==" ":
                stack.append(temp)
                temp=""
            else:
                temp+=x
        if len(temp)!=0:
            stack.append(temp)
        newword = ""
        while stack:
            y = stack.pop()
            if len(newword)==0:
                newword+=y
            else:
                newword+=" "+y
        return (newword)
