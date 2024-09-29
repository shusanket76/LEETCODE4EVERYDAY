class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sumwehave = 0
        for x in rolls:
            sumwehave +=x
        
        total = mean * (len(rolls)+n)
    
        total -= sumwehave

        if total<n or total>6*n:
            return []

        result = [1 for x in range(n)]
        total-=n
        for y in range(n):
            addvalue = min(5, total)
            result[y]+=addvalue
            total-=addvalue
        return result 
        