# -*- coding: utf-8 -*-
# File  : 4.py
# Author: HuWenBo
# Date  : 2018/10/29
# 题目4：两个排序数组的中位数


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # 用了Python自带的sort排序，时间复杂度好像不符合要求，但是能过。。
        # 时间复杂度：O(nlogn)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = nums1 + nums2
        res.sort()
        n = len(res) // 2
        return res[n] if len(res) % 2 == 1 else (res[n] + res[n - 1]) / 2

    def findMedianSortedArrays1(self, nums1, nums2):
        """
        将两个有序数组合并为一个有序数组，这是归并排序的关键步骤。
        因为两个数组都是有序的，所以一次线性循环就ok了，复杂度为O(n)
        :param nums1:
        :param nums2:
        :return:
        """
        temp = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                temp.append(nums1.pop(0))
            else:
                temp.append(nums2.pop(0))
        temp.extend(nums1)
        temp.extend(nums2)
        n = len(temp) // 2
        return temp[n] if len(temp) % 2 == 1 else (temp[n] + temp[n - 1]) / 2
