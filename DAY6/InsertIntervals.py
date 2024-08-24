class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for x in range(1, len(intervals)):
            newInterval = intervals[x]
            if res[-1][1] >= newInterval[0]:
                res[-1] = [min(res[-1][0], newInterval[0]), max(res[-1][1], newInterval[1])]
            else:
                res.append(newInterval)
        return res
        