# -*- coding: utf-8 -*-
# File  : 13.py
# Author: HuWenBo
# Date  : 2018/11/4
class Solution:
    def romanToInt(self, s):
        """
        将定义的和特殊定义的都放在字典序中。
        首先一开始读取两个判断是否在特殊定义里面，如果不在就判断是否在普通定义里面，然后相加。
        :type s: str
        :rtype: int
        """
        s_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        flag = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        i, result = 0, 0
        s_len = len(s)
        if s_len == 1:
            return s_dict.get(s[0])
        while i < s_len:
            if s[i:i + 2] in flag:
                result += flag.get(s[i:i + 2])
                i += 2
            else:
                result += s_dict.get(s[i])
                i += 1
            print(result)
        return result

    def romanToInt(self, s):
        """
        题目给出的罗马数字都是正确的。
        所以我们可以从0开始判断，当前的如果比下一个小的话就说明这两个连续的是特殊的整数。
        s[n] > s[n+1] 说明当前s[n]代表一个数
        s[n] < s[n+1] 说明s[n]和s[n+1]组成一个数
        因为正常的罗马数组，是从左到右是从大到小排列的。
        :param s:
        :return:
        """
        ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if not s:
            return 0
        num = 0
        for i in range(len(s) - 1):
            if ROMAN[s[i]] < ROMAN[s[i + 1]]:
                num -= ROMAN[s[i]]
            else:
                num += ROMAN[s[i]]
        return num + ROMAN[s[-1]]


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt("MCMXCIV"))
