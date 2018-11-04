# -*- coding: utf-8 -*-
# File  : 17.py
# Author: HuWenBo
# Date  : 2018/11/4
# 017：电话号码的字母组合
class Solution:
    def letterCombinations(self, digits):
        """
        采用递归的方式，来进行排列组合
        :type digits: str
        :rtype: List[str]
        """
        flag = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []

        def _sub(nums, res):
            if not nums:
                return res
            res = [a + b for a in res for b in flag.get(nums[0])]
            return _sub(nums[1:], res)

        return _sub(digits, [''])


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('23'))
