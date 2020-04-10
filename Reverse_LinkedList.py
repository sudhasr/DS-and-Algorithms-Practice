""" Reverse a singly linked list  
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL  """

""" Note: 1. Always store given head in another variable for not losing track of it
		  2. Create dummy head in order to come back to first node for returning  """

# Approach1: Iterative approach using a stack
# 1. Traverse through the given linked list and keep pushing the values into a stack
# 2. Once curr == Null, pop the elements from the stack until the stack is empty AND create new Linked list nodes while popping.
# 3. Return dummy node new_head's next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        stack = []
        # 1.        
        while curr:
            stack.append(curr.val)
            curr = curr.next
            #|  5   |
            #|  4   |
            #|  3   |
            #|  2   |
            #|__1___|
        # 2.  
        new_head = node = ListNode(None)            #   dummy head
        while stack:
            node.next = ListNode(stack.pop())       #   dummy head's next points to first reversed node we create
            node = node.next                        #   reversed using dummy head "node" 5->4->3->2->1->NULL
        # 3.
        return new_head.next                        #   dummy head "new_head's" next points to first node new_head->5->4->3->2->1->NULL
		
#Time Complexity - O(2N) where N is number of nodes =>O(N) for LinkedList traversal and O(N) for pop operation and creation of new nodes
#Space complexity - O(N) as we use a stack

#Approach2: Iterative approach using pointers
# 1. Create prev pointer and initiate to NULL and store head in curr
# 2. Traverse the LinkedList, in a loop, store the curr's next in temp, 
#    point curr's next to prev, move prev to curr and curr to temp
# 3. In the end Return prev as it will be pointing to the first node of reversed list 

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
		# 1.
        curr = head
        prev = None
		# 2. 
        while curr:
            temp = curr.next		
            curr.next  = prev
            prev = curr
            curr = temp			
			# After first iteration NULL<- 1       2->3->4->5->NULL
			#							   ^       ^
			#							 prev   temp,curr 
        #3.
		return prev
		
#Time Complexity - O(N) where N is number of nodes
#Space Complexity - O(1)

#Approach3: Recursive approach
# 1. Curr points to head node
# 2. Call recursive function by passing curr.next as head and until we reach end (base case)
# 3. When we hit base case, return new_head to previous recursive call 
# 4. Change curr.next.next pointer to present head (reverse operation), curr.next to Null(unlink) and return new_head

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        
        #Base Case
        if curr == None or curr.next == None:
            return curr
        
        #Recursion logic
        new_head = self.reverseList(curr.next)
        curr.next.next = head
        curr.next = None
        return new_head
		
#Time Complexity - O(2N) where N is number of nodes
#Space Complexity - O(N) if we consider recursive stack, otherwise O(1)