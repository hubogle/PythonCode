# -*- coding: utf-8 -*-
# File  : 43.py
# Author: HuWenBo
# Date  : 2018/11/1
# 043：字符串相乘
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        arr = [0] * (len(num1) + len(num2))
