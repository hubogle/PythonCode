# -*- coding: utf-8 -*-
# File  : 5.py
# Author: HuWenBo
# Date  : 2018/10/31
# 题目5：最长回文子串
class Solution:
    def longestPalindrome(self, s):
        """
        暴力枚举，枚举所有字符串的起点，逐一判断是否是回文字符串。
        总共有n(n-1)/2的字符串，验证字符串要O(n)
        时间复杂度：O(n^3)
        空间复杂度：O(1)
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        max_count = 0
        result = ''
        for i in range(s_len):
            for j in range(i, s_len):
                count = 0
                left, right = i, j
                while right >= left:
                    if s[right] == s[left]:
                        left, right = left + 1, right - 1
                    else:
                        break
                if right < left:  # 当[i,j]区间符合条件，就获取长度。
                    count = j - i + 1
                if count > max_count:
                    max_count = count
                    result = s[i:j + 1]
        return result

    def longestPalindrome1(self, s):
        """
        枚举子串中心
        将字符串从中心枚举，需要判断字符串的奇偶性
        不断从中心向周围扩展
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        :param s:
        :return:
        """
        max_count = 0
        s_len = len(s)  # 字符串长度
        result = ''
        if s_len == 1:
            return s
        for i in range(s_len - 1):
            count = 1  # 当是奇数的时候，初试长度为1
            for k in range(1, i + 1):
                left, right = i - k, i + k  # 不断从中心向外面扩展
                if left >= 0 and right < s_len:  # 判断相等长度就加2
                    if s[left] == s[right]:
                        count += 2
                    else:
                        break
            if count > max_count:
                max_count = count
                result = s[i - count // 2:i + count // 2 + 1]
            if s[i] == s[i + 1]:  # 处理偶数字串
                count = 2  # 一开始就处理偶数字符串，两个相邻元素作为整体, 一开始count=2， j指向下一个相同的字符串
                for k in range(1, i + 1):  # 处理左边字符串的全部长度(i+1)
                    left, right = i - k, i + k + 1  # left左边等于i - k，right右边等于i + 1 + k
                    if (left >= 0) & (right < s_len):
                        if s[left] == s[right]:
                            count += 2
                        else:
                            break
                if count > max_count:
                    max_count = count
                    result = s[i - count // 2 + 1:i + count // 2 + 1]
        return result

    def longestPalindrome2(self, s):
        """
        manacher算法
        参考https://segmentfault.com/a/1190000008484167
        :param s:
        :return:
        """
        s = '#' + '#'.join(s) + '#'
        s_len = len(s)
        f = []
        maxj = 0
        maxl = 0
        maxd = 0


solution = Solution()
print(solution.longestPalindrome1('acca'))
