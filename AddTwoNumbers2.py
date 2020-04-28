"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""
"""
Approach: 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. Reverse the two linked lists (reverse function)
        h1 = self.reverse(l1)
        h2 = self.reverse(l2)
        
        # 2. Create dummy nodes
        dummy = ListNode(None)
        
        # 3. Traverse the lists and add values of each nodes to 'summ' until both lists reaches Null or carry value becomes zero
        summ = 0
        while h1 or h2 or summ:
            if h1:
                summ += h1.val
                h1 = h1.next
            if h2:
                summ += h2.val
                h2 = h2.next
             # 4. At each iteration check for carry and create result nodes and do in-place reverse
            dummy.val = summ%10
            result = ListNode(summ//10)
            result.next = dummy
            dummy = result
            summ = summ//10
        if result.val == 0:
            return result.next
        else:
            return result
        
    # Reverse function
    def reverse(self, head):
        node = head
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev