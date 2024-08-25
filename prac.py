def reverseWords(s: str) -> str:
        slist = s.split(" ")
        stack = []
        for x in slist:
            if x!=" ":
                stack.append(x)
        newword = ""
        count = 0
        while stack:
            y = stack.pop()
            
            if len(newword)==0:
                newword+=y
            else:
                newword+=" "+y
 
        return (newword)
a = reverseWords("  hello world  ")
print("=>"+a+"<=")