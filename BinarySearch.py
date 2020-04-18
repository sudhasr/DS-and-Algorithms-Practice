""" Binary Search algorithm """

# Recursive approach

class Solution:
	def binarySearch(self, nums, target):				
		# recursion helper for binarySearch
		return self.helper(nums, 0, len(nums)-1, target)
		
		
	def helper(self, nums, l, h, target):
		if l>=h:
			return -1
		else:	
			mid = h-l//2
			if nums[mid] < target:
				return self.helper(nums, mid+1, h, target)
			elif nums[mid] > target:
				return self.helper(nums, l, mid-1, target)
			else:
				return mid
			
# Iterative approach
class Solution:
	def binarySearch(self, nums, target):
		low = 0
		high = len(nums)-1
		while low < high:
			mid = high-low//2
			if nums[mid] < target:
				low = mid+1
			elif nums[mid] > target:
				high = mid-1
			else:
				return mid
		return -1

nums = [2, 5, 8, 21, 45, 68, 95]
#nums = [1,1,1,1,1]
target = 8
bs = Solution()
index = bs.binarySearch(nums, target)
print(index)