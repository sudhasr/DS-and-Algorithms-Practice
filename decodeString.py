"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
s = "3[ab4[2[d]]]", return "abddddddddabddddddddabdddddddd"
"""

"""
Approach1: Using two stacks
1. Create two stacks, one to store number and another to store string
2. There are four cases to handle, 1. if it is a digit, 2. if it is an alphaber, 3. if it is '[', and 4. if it is a ']'
3. Traverse the input string and check for thse 4 cases 
4. Keep updating the curr_num and curr_str while encountering numbers and alphabets, push these values to the respective stacks when '[' is found 
and reset the curr_num and curr_str variables
5. When ']' is found, pop from num_stack as we need to process curr that many times, store processed string in new_str, pop element from str_stack and add it to new_str
	Store this latest string in curr variable as we will be processing this later when we encounter another ']'
6. Final string will be stored in curr_str
"""

#Time Complexity: O(N) where N is length of the 'output string'
#Space Compelxity: O(N) for stacks split into two => ex. worst case we have '1a1b1c1d'

class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        curr_num = 0
        curr_str = ''
        
        for c in s:
            # Case 1: Process the digit
            if c.isdigit():
                curr_num = curr_num*10 + (ord(c) - ord('0'))
            
            # Case 2: Open bracket
            elif c == '[':
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_num = 0
                curr_str = ''
            
            # Case 3: Process string
            elif c.isalpha():
                curr_str += c
            
            # Case 4: Close bracket
            else:
                # if c == ']':
                times = num_stack.pop()
                new_str = ''
                #char = str_stack.pop()
                while times>0:
                    new_str += curr_str
                    times -= 1
                curr_str = str_stack.pop()
                curr_str += new_str
        return curr_str
		
		
"""
Approach2: Using one stack
1. Follow same steps as Approach1, but instead of two create a single stack to store both num and alphabet
2. Here order of pushing intot the stack matters. I want to pop digit first, process the curr_str that many times and only then
	append processed str to the previous_str. This makes sense to push curr_str first and then curr_num into the stack
3. Rest if the steos are the same
"""
#Time Complexity: O(N) where N is length of the 'output string'
#Space Compelxity: O(N) for stacks

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ''
        for c in s:
            # Case 1: if it is a digit
            if c.isdigit():
                curr_num = curr_num*10 + (ord(c)-ord('0'))
            
            # Case 2: If it is a '['
            elif c == '[':
                # Here order of pushing inside the stack matters
                # First push current string and then the current number, so that when popped,
                # the number comes first for prcessing the curr_str of that time
                stack.append(curr_str)
                stack.append(curr_num)
                curr_num = 0
                curr_str = ''
            
            # Case 3: If it is an alphabet or a space
            elif c.isalpha() or c.isspace():
                curr_str += c
            
            # Case 4: If it a ']'
            else:
                times = stack.pop()
                new_str = ''
                while times>0:
                    new_str += curr_str
                    times -= 1
                curr_str = stack.pop()
                curr_str += new_str
        return curr_str

"""
VARIATION: If space is present in between alphabets
1. In the if condition to check for alphabet, add an 'or' condition to check if it s space and then append it to curr_str
"""
class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        curr_num = 0
        curr_str = ''
        for c in s:
            # Case 1: if it is a digit
            if c.isdigit():
                curr_num = curr_num*10 + (ord(c)-ord('0'))
            
            # Case 2: If it is a '['
            elif c == '[':
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_num = 0
                curr_str = ''
            
            # Case 3: If it is an alphabet or a space
            elif c.isalpha() or c.isspace():
                curr_str += c
            
            # Case 4: If it a ']'
            else:
                times = num_stack.pop()
                new_str = ''
                while times>0:
                    new_str += curr_str
                    times -= 1
                curr_str = str_stack.pop()
                curr_str += new_str
        return curr_str