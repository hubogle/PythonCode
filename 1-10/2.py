# -*- coding: utf-8 -*-
# File  : 2.py
# Author: HuWenBo
# Date  : 2018/10/28
# 题目2：两数相加

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        将l1和l2遍历完取整数然后相加。
        将l3构建一个链表
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ln1, ln2 = '', ''
        while l1:
            ln1 += str(l1.val)
            l1 = l1.next
        while l2:
            ln2 += str(l2.val)
            l2 = l2.next
        add = str(int(ln1[::-1]) + int(ln2[::-1]))[::-1]
        head = ListNode(add[0])
        result = head
        for i in range(1, len(add)):
            node = ListNode(add[i])
            head.next = node
            head = head.next
        return result

    def addTwoNumbers1(self, l1, l2):
        """

        :param l1:
        :param l2:
        :return:
        """
        head = ListNode(0)  # 创建一个新节点
        head.next = l1
        carry = 0
        while l1 and l2:  # 将l1节点和l2共有的节点相加
            sum = l1.val + l2.val + carry
            val, carry = sum % 10, sum // 10
            l1.val = val
            prev, l1, l2 = l1, l1.next, l2.next

        l = l1 or l2
        prev.next = l
        while l and carry:  # 将l1和l2非共有节点和余数相加
            sum = l.val + carry
            val, carry = sum % 10, sum // 10
            l.val = val
            prev, l = l, l.next
        if carry:  # 添加余数节点
            prev.next = ListNode(carry)
        return head.next
