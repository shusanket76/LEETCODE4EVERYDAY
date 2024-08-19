class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for x in range(1,len(intervals)):
            last = res[-1]
            lasty = last[1]
            curr = intervals[x]
            currx = curr[0]
            if lasty<currx:
                res.append(intervals[x])
            else:
                res[-1][1] = max(last[1], curr[1])
        return res