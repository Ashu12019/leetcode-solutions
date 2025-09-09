class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            # calculate width
            width = r - l
            
            # check which line is smaller
            if height[l] < height[r]:
                res = max(res, width * height[l])
                l += 1
            else:
                res = max(res, width * height[r])
                r -= 1

        return res
