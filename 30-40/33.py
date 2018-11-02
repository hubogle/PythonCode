# -*- coding: utf-8 -*-
# File  : 33.py
# Author: HuWenBo
# Date  : 2018/11/1
# 033：搜索旋转排序数组
class Solution:
    def search(self, nums, target):
        """
        二分查找的扩展
        在原来的二分查找里，mid的两边都是有序的，但是这个题中mid至少有一遍是有序的
        有可能左边，有可能右边，或都有序。
        我们在有序的一边查找，判断target是在有序的一遍还是无序的一遍。
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[left]:  # 左边有序
                if nums[mid] > target >= nums[left]:  # 有序的一边
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 右边有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
