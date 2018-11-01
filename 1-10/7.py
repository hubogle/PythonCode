# -*- coding: utf-8 -*-
# File  : 7.py
# Author: HuWenBo
# Date  : 2018/11/1
# 007：反转整数
class Solution:
    def reverse(self, x):
        """
        利用栈的特性来进行倒置
        :type x: int
        :rtype: int
        """
        flag = 1
        result = []
        x_sum = 0
        if x < 0:
            flag = -1
            x = abs(x)
        while x:
            n = x % 10
            result.append(n)
            x //= 10
        while result:
            n = result.pop(0)
            x_sum = x_sum * 10 + n
        x_sum = x_sum * flag
        if x_sum < -2 ** 31 or x_sum > 2 ** 31 - 1:
            return 0
        else:
            return x_sum

    def reverse1(self, x):
        """
        利用循环，主要是最后一步，使用了bit_length()方法来判断这个数位的长度
        :param x:
        :return:
        """
        rev = 0
        flag = 1
        if x < 0:
            flag = -1
            x = abs(x)
        while x != 0:
            pop = x % 10
            x //= 10
            rev = rev * 10 + pop
        rev = rev * flag
        return rev if rev.bit_length() < 32 else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse1(-123))
