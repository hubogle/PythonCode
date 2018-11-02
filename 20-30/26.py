# -*- coding: utf-8 -*-
# File  : 26.py
# Author: HuWenBo
# Date  : 2018/11/1
# 026：删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums):
        """
        设置两个指针，i是慢指针，j是快指针。
        当nums[i] == nums[j]，就增加j跳过重复项。

        当nums[i] != nums[j] 跳过的重复项已经解说，我们把nums[j]的值复制到nums[i+1]
        然后递增i，接着重复相同的过程
        时间复杂度：O(n)
        空间复杂度：O(1)
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        i = 0
        for j in range(1, len(nums)):  # 也就是到最后前i+1个数都是不重复的
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    solution = Solution()
    solution.removeDuplicates([1, 1, 2, 2, 3, 3])
