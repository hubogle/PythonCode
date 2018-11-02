# -*- coding: utf-8 -*-
# File  : 11.py
# Author: HuWenBo
# Date  : 2018/11/1
# 011：盛最多水的容器
class Solution:
    def maxArea(self, height):
        """
        暴力方法：
        时间复杂度：O(n^2) 计算所有的n(n-1)/2的组合
        :type height: List[int]
        :rtype: int
        """
        max_sum = 0
        for i in range(len(height)):
            for j in range(len(height)):
                max_sum = max(max_sum, min(height[i], height[j]) * (j - i))
        return max_sum

    def maxArea1(self, height):
        """
        left指向最左边，right指向最右面。
        两者向内侧移动，将left和right两者最短的线条向内侧移动，因为移动短的水平长度减小，但缺有利垂直长度增加。
        时间复杂度：O(n)
        :param height:
        :return:
        """
        max_sum = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_sum = max(max_sum, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_sum

    def maxArea2(self, height):
        """
        left指向左边， right指向右边
        只是移动条件是，寻找比当前的长度更长。
        :param height:
        :return:
        """
        water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            water = max(water, (right - left) * h)
            while height[left] <= h and left < right:  # 寻找左边比当前长度更长的。
                left += 1
            while height[right] <= h and left < right:  # 寻找右边比当前长度更长的
                right -= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea1([1, 8, 6, 2, 5, 4, 8, 3, 7]))
