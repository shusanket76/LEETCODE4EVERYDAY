class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        reminders = [0 for x in range(k+1)]

        for x in arr:
            val = ((x%k)+k)%k
            reminders[val]+=1
        print(reminders)
        for y in range(k):
            if y==0:
                if reminders[y]%2!=0:
                    return False
            else:
                print(y)
                if reminders[y]!=reminders[k-y]:
                    return False 

        return True
        