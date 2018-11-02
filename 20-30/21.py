# -*- coding: utf-8 -*-
# File  : 21.py
# Author: HuWenBo
# Date  : 2018/11/1
# 021：合并两个有序链表


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        将l1和l2链表的数据放在列表中
        将列表的数据进行排序，然后构建链表
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t1 = []
        t2 = []
        while l1:
            t1.append(l1.val)
            l1 = l1.next
        while l2:
            t2.append(l2.val)
            l2 = l2.next
        t1.extend(t2)
        t1.sort()
        res = tmp = ListNode(0)
        for i in t1:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next

    def mergeTwoLists1(self, l1, l2):
        """
        创建一个起始节点，将l1和l2节点进行判断后，链接在起始节点后面。

        :param l1:
        :param l2:
        :return:
        """
        head = temp = ListNode(0)
        while l1 and l2:  # 将节点添加在起始节点后面
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2  # 当l1或l2为空的时候直接链接后面的节点
        return head.next

    def mergeTwoLists2(self, l1, l2):
        """
        递归的方法
        :param l1:
        :param l2:
        :return:
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2
