# Implementing priority queue using List data structure

li = []

li.append((1, "a"))
li.append((4, "k"))
li.append((3, "l"))
li.append((9, "u"))

print("Original list: ", li) #[(1,"a"), (4, "k"), (3, "l"), (9, "u")]
# the above code is an example of normal list 

""" 
Sorting the list for every insertn after the first element 

Time Complexity - O(nlogn)

"""
pq = []

pq.append((1, "a"))
pq.append((4, "k"))
pq.sort(reverse=True)
pq.append((3, "l"))
pq.sort(reverse=True)
pq.append((9, "u"))
pq.sort(reverse=True)

while pq:
    print("PQ using list: ", pq.pop(0))

"""
Priority Queue using heapq Module

Time Complexity - O(logn)

"""
import heapq

new_pq = []

for i in range(len(li)):
    heapq.heappush(new_pq, li[i])

while new_pq:
    print("PQ using heapq module: ", heapq.heappop(new_pq))

"""
Priority Queue using queue.PriorityQueue class

Time Complexity - O(logN)

"""
from queue import PriorityQueue

q = PriorityQueue()

for i in range(len(li)):
    q.put(li[i])
while q:
    print(" PQ using Priority Queue class: ", q.get())