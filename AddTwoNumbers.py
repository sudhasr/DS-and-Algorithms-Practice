# 2. Add Two Numbers

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

# Time Complexity - O(maxLength) maxLength is the maximum length between two nodes
# Space Complexity - O(N) as we are creating new linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        dummy = new_head = ListNode(None)
        summ = 0
        while node1 or node2 or summ:
            if node1:
                summ = summ + node1.val
                node1 = node1.next
            if node2:
                summ = summ + node2.val
                node2 = node2.next
            dummy.next = ListNode(summ%10)
            dummy = dummy.next
            summ = summ//10
        return new_head.next