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
# =================================================================================
# 2nd method
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         l = 0 
#         res = []
#         while l<len(intervals):
#             if newInterval[1]<intervals[l][0]:
#                 res.append(newInterval)
#                 return res+intervals[l:]
#             elif intervals[l][1]<newInterval[0]:
#                 res.append(intervals[l])
#             else:
#                 newInterval = [min(newInterval[0], intervals[l][0]), max(newInterval[1], intervals[l][1])]
#             l+=1
        
#         res.append(newInterval)
#         return res
        