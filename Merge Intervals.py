class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        answer = []
        for i in range(1,len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1],end)
            else:
                answer.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        answer.append([start, end])
        return answer
