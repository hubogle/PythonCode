# -*- coding: utf-8 -*-
# File  : 15.py
# Author: HuWenBo
# Date  : 2018/11/1
# 015：三数之和
class Solution:
    def threeSum(self, nums):
        """
        将判断三数之和变为寻找两数之和，但是超时。。
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        check = set()
        for i, num in enumerate(nums):
            target = 0 - num
            dic = set()
            for k, v in enumerate(nums[i + 1:]):
                if not v in dic:
                    dic.add(target - v)
                else:
                    tmp = [num, target - v, v]
                    stmp = ''.join([str(k) for k in tmp])
                    if not stmp in check:
                        check.add(stmp)
                        res.append(tmp)
                    else:
                        continue
        return res

    def threeSum1(self, nums):
        """
        需要求的就是a + = (-c)然后在余下的链表里做两数相加就可以。
        注意数据的去重
        当i和i-1相同就可以跳过
        接下来就是while循环寻找和为0的数据
        :param nums:
        :return:
        """
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    flag = nums[left] + nums[right] + nums[i]
                    if flag == 0:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif flag < 0:
                        left += 1
                    else:
                        right -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [-1,-2,3]
    print(solution.threeSum1(nums))
