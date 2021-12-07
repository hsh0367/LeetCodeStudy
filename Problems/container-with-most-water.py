class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        lp = 0
        rp = len(height) - 1
        while lp < rp:
            if height[lp] < height[rp]:
                area = max(area, (rp - lp) * height[lp])
                lp += 1
            elif height[rp] <= height[lp]:
                area = max(area, (rp - lp) * height[rp])
                rp -= 1
        return area
