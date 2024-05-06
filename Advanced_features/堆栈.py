"""
堆
堆是一种特殊的完全二叉树，所有的节点都满足堆的性质。在一个最大堆中，每个节点的值都不小于其子节点的值；在一个最小堆中，
每个节点的值都不大于其子节点的值。Python的 heapq 模块提供了创建最小堆的功能，并且可以使用它来进行堆排序。
"""
# 堆示例代码（最小堆）
import heapq

min_heap = []
# heapq.heappush 用于向堆中添加元素
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)

while min_heap:
    # heapq.heappop用于移除并返回堆中的最小元素
    smallest = heapq.heappop(min_heap)
    print(smallest)