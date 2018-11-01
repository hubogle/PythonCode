# -*- coding: utf-8 -*-
# File  : 8.py
# Author: HuWenBo
# Date  : 2018/11/1
# 008：字符串转整数
class Solution:
    def myAtoi(self, str):
        """
        常规的从开始遍历
        :type str: str
        :rtype: int
        """
        str = str.strip()
        flag = list('0123456789')
        demo = 1
        result = 0
        if len(str) < 1:
            return 0
        if (str[0] not in flag) and (str[0] not in list('-+')):
            return 0
        if str[0] == '-':
            demo = -1
        elif str[0] == '+':
            demo = 1
        else:
            result = int(str[0])
        for i in range(1, len(str)):
            if str[i] in flag:
                result = result * 10 + int(str[i])
            else:
                break
        result = result * demo
        if result.bit_length() > 31:
            if result > 0:
                return 2 ** 31 - 1
            else:
                return - 2 ** 31
        else:
            return result

    def myAto(self, str):
        """
        正则匹配出正数
        :param str:
        :return:
        """
        import re
        pattern = r'[\s]*[+-]?[\d]+'
        math = re.match(pattern, str)
        if math:
            res = int(math.group(0))
            if res > 2 ** 31 - 1:
                res = 2 ** 31 - 1
            if res < -2 ** 31:
                res = -2 ** 31
        else:
            res = 0
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi('+1'))
