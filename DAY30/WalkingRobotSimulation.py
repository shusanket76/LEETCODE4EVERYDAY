class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dir = 'N'
        cord = [0,0]
        pointer = 1
        sign = "+"
        hasmap = {}
        res = 0
        
        for y in obstacles:
            hasmap[(y[0], y[1])] = True
        
        for x in commands:

            if dir=="N":
                if x==-1:
                    pointer = 0
                    dir = "E"
                elif x==-2:
                    pointer = 0
                    dir = "W"
                else:
                    while x>0:
                        cord[pointer]+=1
                        if (cord[0], cord[1]) in hasmap:
                            cord[pointer]-=1
                            break 
                        x-=1

            elif dir =="E":
                if x==-1:
                    dir = "S"
                    pointer = 1
                elif x==-2:
                    dir = "N"
                    pointer = 1
                else:
                    while x>0:
                        cord[pointer]+=1
                        if (cord[0], cord[1]) in hasmap:
                            cord[pointer]-=1
                            break 
                        x-=1
            elif dir =="W":
                if x==-1:
                    dir="N"
                    pointer = 1

                elif x==-2:
                    dir = "S"
                    pointer = 1
                else:
                    while x>0:
                        cord[pointer]-=1
                        if (cord[0], cord[1]) in hasmap:
                            cord[pointer]+=1
                            break 
                        x-=1
            else:
                if x==-1:
                    dir = "W"
                    pointer = 0
                elif x==-2:
                    dir = "E"
                    pointer = 0
                else:
                    while x>0:
                        cord[pointer]-=1
                        if (cord[0], cord[1]) in hasmap:
                            cord[pointer]+=1
                            break 
                        x-=1
            res = max(res, cord[0]**2+cord[1]**2)
      
    
        return res