# -*- coding: utf-8 -*-
# File  : 1.py
# Author: HuWenBo
# Date  : 2018/10/28
# 题目1：两数之和

class Solution:
    def twoSum(self, nums, target):
        """
        暴力循环
        时间复杂度：O(n^2)
        :type nums: List[int] 整数数组
        :type target: int   目标值
        :rtype: List[int]   返回整数数组的下标
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum1(self, nums, target):
        """
        一遍哈希表 Python 中直接使用 Dict 来存储元素和坐标。
        将数据进行迭代插入到表中的同时，还会检查表中是否存在当前目标元素。
        时间复杂度：O(n)
        :param nums:
        :param target:
        :return:
        """
        map = {}
        for i in range(len(nums)):
            number = target - nums[i]
            if number in map:
                return [map[number], i]
            map[nums[i]] = i


solution = Solution()
result = solution.twoSum1([3, 7, 11, 4], 7)
print(result)