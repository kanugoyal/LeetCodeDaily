class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxWidth = 0; points.sort()
        pts = len(points)-1
        for i in range(pts):
            currWidth = abs(points[i][0]- points[i+1][0])
            if currWidth > maxWidth:
                maxWidth = currWidth
            
        return maxWidth