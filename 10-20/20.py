# -*- coding: utf-8 -*-
# File  : 20.py
# Author: HuWenBo
# Date  : 2018/11/1
# 020：有效的括号
class Solution:
    def isValid(self, s):
        """
        利用字典序列，和栈的特性进行
        :type s: str
        :rtype: bool
        """
        if len(s) % 2:
            return False
        temp = {')': '(', '}': '{', ']': '['}
        demo = []
        for i in s:
            if i not in temp:
                demo.append(i)
            if i in temp and demo:
                flag = demo.pop()
                if flag == temp.get(i):
                    continue
                else:
                    demo.extend([flag, i])
        return demo == []

    def isValid1(self, s):
        """
        优化后
        :param s:
        :return:
        """
        if len(s) % 2:
            return False
        stack = []
        temp = {')': ')', '[': ']', '{': '}'}
        for i in s:
            if i in temp:
                stack.append(i)
            else:
                if not stack or temp[stack.pop()] != i:  # 当栈为空，还有右括号，或者有右括号但是从栈弹出的左括号和右不匹配
                    return False
        return stack == []


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid1('}'))
