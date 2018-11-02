# -*- coding: utf-8 -*-
# File  : 14.py
# Author: HuWenBo
# Date  : 2018/11/1
# 014：最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs):
        """
        编写一个函数来查找字符串数组中的最长公共前缀。
        如果不存在公共前缀，返回空字符串 ""。

        主要用了Python的解包，和zip将可迭代对象打包成一个tuple(元组)
        还是用了enumerate()函数，将一个可遍历的数据对象，组合为一个索引序列，同时列出数据和数据下标。
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for k, v in enumerate(zip(*strs)):
            if len(set(v)) > 1:
                return strs[0][:k]
        return min(strs, key=len)  # 当最短的字符串已经遍历完，直接返回最短的就可以了

    def longestCommonPrefix(self, strs):
        """
        常规解法，先找到最短的字符串，然后将其他的字符串，进行循环遍历寻找相同的字符串。
        :param strs:
        :return:
        """
        if not strs:
            return ''
        short_str = min(strs, key=len)
        for k, v in enumerate(short_str):
            for i in strs:
                if i[k] != v:
                    return short_str[:k]
        return short_str


if __name__ == '__main__':
    sol = Solution()
    demo = ['ab', 'ab', 'ab', 'ab', 'ab']
    sol.longestCommonPrefix(demo)
