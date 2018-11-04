# -*- coding: utf-8 -*-
# File  : 46.py
# Author: HuWenBo
# Date  : 2018/11/4
# 046：全排列
class Solution:
    def permute(self, nums):
        """
        深度搜索
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        sub = []
        self.dfs(nums, sub)
        return self.result

    def dfs(self, nums, sub):
        """
        这里的sub是局部变量，将sub数据拷贝，才能保存。
        :param nums:
        :param sub:
        :return:
        """
        if len(nums) == len(sub):  # 当sub和nums长度相同时就排列完成
            self.result.append(sub.copy())
        for i in nums:
            if i in sub:
                continue
            sub.append(i)
            self.dfs(nums, sub)
            sub.remove(i)

    def permute1(self, nums):
        """
        递归排序
        :param nums:
        :return:
        """
        if len(nums) <= 1:
            return [nums]
        ans = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i + 1:]
            for temp in self.permute1(n):
                ans.append([num] + temp)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute1([1, 2, 3]))
