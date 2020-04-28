"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

"""

"""
Approach3: Two pointers




"""
# Time Complexity - O(N + k)
# Space Complexity - O(1)
"""
List has a cycle:
We break down the movement of the slow pointer into two steps, the non-cyclic part and the cyclic part:

The slow pointer takes "non-cyclic length" steps to enter the cycle. At this point, the fast pointer has already reached the cycle. \text{Number of iterations} = \text{non-cyclic length} = NNumber of iterations=non-cyclic length=N

Both pointers are now in the cycle. Consider two runners running in a cycle - the fast runner moves 2 steps while the slow runner moves 1 steps at a time. Since the speed difference is 1, it takes \dfrac{\text{distance between the 2 runners}}{\text{difference of speed}} 
difference of speed
distance between the 2 runners
​	
  loops for the fast runner to catch up with the slow runner. As the distance is at most "\text{cyclic length K}cyclic length K" and the speed difference is 1, we conclude that
\text{Number of iterations} = \text{almost}Number of iterations=almost "\text{cyclic length K}cyclic length K".

Therefore, the worst case time complexity is O(N+K)O(N+K), which is O(n)O(n).
""" 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Edge Case
        if head == None or head.next == None:
            return False
        # Two pointers approach
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False