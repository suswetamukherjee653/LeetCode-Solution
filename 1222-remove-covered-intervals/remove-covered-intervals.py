class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count=0
        end_num=0
        for start,end in intervals:
            if end > end_num:
                count += 1
                end_num=end

        return count
        