"""
堆是二叉树，是标识符固定的
heapq.heapify(x) ---- 将list x 转换成堆
heapq.heappush(heap, item) ---- 将item的值加入heap中，保持堆的不变性
heapq.heappop(heap) ---- 弹出并返回heap的最小元素，保持堆的不变性。使用heap[0], 可以只访问最小的元素而不弹出它。
"""
import heapq
x = [4, 5, 6, 7, 9, 1, 2, 3, 0]
print(x)
heapq.heapify(x)
print(x)

heapq.heappush(x, 2)
print(x)

heapq.heappop(x)
print(x)