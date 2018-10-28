# -*- coding: utf-8 -*-
# File  : 3.py
# Author: HuWenBo
# Date  : 2018/10/28
# 题目3：无重复字符的最长子串

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        暴力方法，直接全部遍历，但是会超时。
        会检验返回在[i, j)的字符是否都是唯一的。
        时间复杂度：O(n^3)
        :type s: str
        :rtype: int
        """
        if not len(s):
            return 0
        result = 1
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                flag = s[i:j]
                if len(set(flag)) == len(flag):
                    result = result if result > len(flag) else len(flag)
        return result

    def lengthOfLongestSubstring1(self, s):
        """
        检查字符串是否重复，设置一个初试字符串flag。
        遍历s字符串，当右边添加一个判断是否重复，当重复的话就删除左边的字符串。
        时间复杂度：O(2n)
        空间复杂度：O(min(m,n))m字符串大小，n字符集的大小
        :param s:
        :return:
        """
        result, i, j = 0, 0, 0
        flag = set()
        while i < len(s) and j < len(s):
            if s[j] not in flag:
                flag.add(s[j])
                j += 1
                result = max(result, j - i)
            else:
                flag.remove(s[i])
                i += 1
        return result

    def lengthOfLongestSubstring2(self, s):
        """
        将方法2进行优化，我们可以记录字符串中字符出现的最后一个位置。
        start：字符串开始的位置，上次同一个字符出现的位置加1
        flag：记录每个字符最后一个位置
        时间复杂度：O(n)
        :param s:
        :return:
        """
        start = max_len = 0
        flag = {}
        for i in range(len(s)):
            if s[i] in flag and start <= flag[s[i]]:
                start = flag[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            flag[s[i]] = i
        return max_len


demo = Solution()
demo.lengthOfLongestSubstring2("assadsadss")
