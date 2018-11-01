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
        可以在O(n)的时间处理出字符串中每个字符为中心的回文串半径，将愿字符串处理成两倍长度的新串，在两个字符间加入一个
        特定的特殊字符，就成了以中间特殊字符为中心的奇数长度的回文串。
        主要是根据已知回文字符串的对称原则，来判断另一个回文字符串。
        参考https://segmentfault.com/a/1190000008484167
        根据回文的性质，s[i]有三种情况
        1）j的回文串有一部分在id之外（id是上一个回文串），不能更长
        2）j的回文串全部在id的内部，不能更长
        3）j的回文串左段正好与id的回文串左端重合，可以更长
        :param s:
        :return:
        """
        s = '#' + '#'.join(s) + '#'  # 将偶数和奇数长度的回文串都变为奇数回文串
        s_len = len(s)
        f = []
        maxj = 0  # 记录对i右边影响最大的字符位置j
        maxl = 0  # 记录j影响范围的右边界
        maxd = 0  # 最长回文子串长度
        for i in range(s_len):
            if maxl > i:  # 判断i是否在属于最大右边界影响的范围
                count = min(maxl - i, f[2 * maxj - i] // 2)  # 判断回文字符串的最大长度，i是关于回文串j的对称点。
            else:  # 不在范围就count就为1
                count = 1
            while i - count >= 0 and i + count < s_len and s[i - count] == s[i + count]:  # s[i]的边界正好和回文串重合
                count += 1
            if i - 1 + count > maxl:  # 当新的右边界影响范围比之前的右边界打，记录影响范围大的边界和序号。
                maxl, maxj = i + count - 1, i
            f.append(count * 2 - 1)  # 记录以i为中心的回文串的长度
            maxd = max(maxd, f[i])  # 最大的回文串长度
        return (maxd + 1) // 2 - 1


solution = Solution()
print(solution.longestPalindrome2('asdsws'))
