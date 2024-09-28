class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = 0
        for x in chalk:
            total+=x
        target = k%total
        print(total)
        idx = 0
        while target>0:
            if chalk[idx]>target:
                return idx
            target-=chalk[idx]
            idx+=1
        return idx
        