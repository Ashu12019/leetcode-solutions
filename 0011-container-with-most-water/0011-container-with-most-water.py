class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            # Calculate current area
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            # Move the pointer with the smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
