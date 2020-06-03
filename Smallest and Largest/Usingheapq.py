import heapq
import time


example_list = [1, 3, 5, 7, 8, 0, 5, 12, 6, 56, 7346, 3431464, 6747, 6, 756,
                34, 32, 412, 31, 42, 5, 234, 24, 5, 234, 5, 4, 32, 5]
print(heapq.nlargest(5, example_list))
print(heapq.nsmallest(5, example_list))

heapq.heapify(example_list)
print(example_list)
objects = heapq.__dict__

print(objects)
