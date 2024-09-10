class Solution:
    def isHappy(self, n: int) -> bool:
        hasmap = {}
        while True:
            a  = str(n)
            temp = 0
            for x in a:
                temp+=int(x)**2
            n = temp
            if n==1:
                return True
                break
            if n in hasmap:
                return False
            hasmap[n]=True

        return False
            