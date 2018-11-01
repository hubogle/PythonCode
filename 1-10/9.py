# -*- coding: utf-8 -*-
# File  : 9.py
# Author: HuWenBo
# Date  : 2018/11/1
# 009：回文数
class Solution:
    def isPalindrome(self, x):
        """
        思路：
        1）将数字转换为字符串，来检查是否是回文，但是需要额外的空间。
        2）将数字本身反转，与原始数字进行比较，但是反转后的数字会益处。
        3）将数字的一半进行反转，与原始数字的前半部分比较。

        :type x: int
        :rtype: bool
        """

        if x < 0 or (x % 10 == 0 and x != 0):  # 小于0，和最后以0结尾的都不是回文
            return False
        rev = 0
        while x > rev:  # 当原始数字小于反转数字后，就处理一半位的数字
            rev = rev * 10 + x % 10
            x //= 10
        # 当x为奇数的时候，可以删除反转后的个位数(回文的中心数字)
        return x == rev or x == rev // 10

    def isPalindrome1(self, x):
        """
        将整数转换为字符串，将字符串进行反转，来进行比较。
        :param x:
        :return:
        """
        return x >= 0 and str(x) == str(x)[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(121))
