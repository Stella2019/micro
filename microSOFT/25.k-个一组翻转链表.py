#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (63.68%)
# Likes:    812
# Dislikes: 0
# Total Accepted:    118.6K
# Total Submissions: 186.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 
# 
# 示例：
# 
# 给你这个链表：1->2->3->4->5
# 
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 
# 
# 
# 说明：
# 
# 
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 
# 
#
前置知识
链表
公司
阿里
腾讯
百度
字节
思路
题意是以 k 个 nodes 为一组进行翻转，返回翻转后的linked list.
从左往右扫描一遍linked list，扫描过程中，以 k 为单位把数组分成若干段，对每一段进行翻转。给定首尾 nodes，如何对链表进行翻转。
链表的翻转过程，初始化一个为null的 previous node（prev），然后遍历链表的同时，当前node （curr）的下一个（next）指向前一个node（prev）， 在改变当前 node 的指向之前，用一个临时变量记录当前 node 的下一个node（curr.next). 即
ListNode temp = curr.next;
curr.next = prev;
prev = curr;
curr = temp;
举例如图：翻转整个链表 1->2->3->4->null -> 4->3->2->1->null

这里是对每一组（k个nodes）进行翻转，
先分组，用一个count变量记录当前节点的个数
用一个start 变量记录当前分组的起始节点位置的前一个节点
用一个end变量记录要翻转的最后一个节点位置
翻转一组（k个nodes）即(start, end) - start and end exclusively。
翻转后，start指向翻转后链表, 区间（start，end）中的最后一个节点, 返回start 节点。
如果不需要翻转，end 就往后移动一个（end=end.next)，每一次移动，都要count+1.
如图所示 步骤 4 和 5： 翻转区间链表区间（start， end）

举例如图，head=[1,2,3,4,5,6,7,8], k = 3

NOTE: 一般情况下对链表的操作，都有可能会引入一个新的dummy node，因为head有可能会改变。这里head 从1->3, dummy (List(0))保持不变。
复杂度分析
时间复杂度: O(n) - n is number of Linked List
空间复杂度: O(1)

关键点分析
创建一个 dummy node
对链表以 k 为单位进行分组，记录每一组的起始和最后节点位置
对每一组进行翻转，更换起始和最后的位置
返回dummy.next.

 
class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode, terminal):
        cur = head
        pre = None
        while cur != terminal:
            next = cur.next
            cur.next = pre

            pre = cur
            cur = next
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ans = ListNode()
        ans.next = head
        pre = ans

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return ans.next
            next = tail.next
            head, tail = self.reverse(head, tail, tail.next)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = next
            pre = tail
            head = next

        return ans.next
 
 
扩展 1
要求从后往前以k个为一组进行翻转。(字节跳动（ByteDance）面试题)
例子，1->2->3->4->5->6->7->8, k = 3,
从后往前以k=3为一组，
6->7->8 为一组翻转为8->7->6，
3->4->5为一组翻转为5->4->3.
1->2只有 2 个 nodes 少于k=3个，不翻转。
最后返回： 1->2->5->4->3->8->7->6
这里的思路跟从前往后以k个为一组进行翻转类似，可以进行预处理：
翻转链表
对翻转后的链表进行从前往后以 k 为一组翻转。
翻转步骤 2 中得到的链表。
例子：1->2->3->4->5->6->7->8, k = 3
翻转链表得到：8->7->6->5->4->3->2->1
以 k 为一组翻转： 6->7->8->3->4->5->2->1
翻转步骤#2 链表： 1->2->5->4->3->8->7->6


扩展 2
如果这道题你按照 92.reverse-linked-list-ii 提到的 p1, p2, p3, p4（四点法） 的思路来思考的话会很清晰。
代码如下（Python）：
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k < 2:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        count = 0
        while cur:
            count += 1
            if count % k == 0:
                pre = self.reverse(pre, cur.next)
                # end 调到下一个位置
                cur = pre.next
            else:
                cur = cur.next
        return dummy.next
    # (p1, p4） 左右都开放

    def reverse(self, p1, p4):
        prev, curr = p1, p1.next
        p2 = curr
        # 反转
        while curr != p4:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # 将反转后的链表添加到原链表中
        # prev 相当于 p3
        p1.next = prev
        p2.next = p4
        # 返回反转前的头， 也就是反转后的尾部
        return p2

# @lc code=end
复杂度分析
时间复杂度：n
空间复杂度：1
相关题目
92.reverse-linked-list-ii
206.reverse-linked-list

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
# @lc code=end

