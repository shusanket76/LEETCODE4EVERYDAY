def numSubarraysWithSum(nums, goal: int) -> int:
        hasmap = {}
        temp = 0
        res=[0]
        for x in nums:
            temp+=x
            if temp==goal:
                res[0]+=1
                # print(temp,x,res)
                weneed = temp-goal
                if weneed in hasmap:
                    res[0]+=hasmap[weneed]
            elif temp<goal:
                if temp in hasmap:
                    hasmap[temp]+=1
                else:
                    hasmap[temp]=1
            else:
                weneed = temp-goal
                if weneed in hasmap:
                    res[0]+=hasmap[weneed]
                if temp in hasmap:
                    hasmap[temp]+=1
                else:
                    hasmap[temp]=1
        return (res[0])

a = numSubarraysWithSum([1,0,1,0,1],2)