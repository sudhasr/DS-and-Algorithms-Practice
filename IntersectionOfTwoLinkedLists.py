# 160. Intersection of Two Linked Lists

"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. 
From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

"""

"""
Approach 1: Brute Force
For each node ai in list A, traverse the entire list B and check if any node in list B coincides with ai.

Complexity Analysis

Time complexity : O(mn)O(mn).

Space complexity : O(1)O(1).


Approach 2: Hash Table
Traverse list A and store the address / reference to each node in a hash set. Then check every node bi in list B: if bi appears in the hash set, then bi is the intersection node.

Complexity Analysis

Time complexity : O(m+n)O(m+n).

Space complexity : O(m)O(m) or O(n)O(n).

"""

"""
Approach 3: Two pointers
"""

# Time Complexity - O(m+n)
# Space Complexity - O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #Edge Case
        if headA == None or headB == None:
            return None
        if headA == headB:
            return headA
        
        curr1 = headA
        curr2 = headB
        # 1. Find the length of both the linked lists
        count1 = 0
        count2 = 0
        while curr1:
            curr1 = curr1.next
            count1 += 1
        while curr2:
            curr2 = curr2.next
            count2 += 1
        # 2. Reposition curr1 and curr2 to headA and headB
        curr1 = headA
        curr2 = headB
        # 3. Move the head of the longer list to the node until both lists are equal in length
        if count1 > count2:
            while count1 > count2:
                curr1 = curr1.next
                count1 -= 1
        else:
            while count2 > count1:
                curr2 = curr2.next
                count2 -= 1
        # 4. Move both the pointers one step until they are equal
        while curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1