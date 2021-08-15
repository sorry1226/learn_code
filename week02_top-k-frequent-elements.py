import collections
import heapq



def topKFrequent(nums, k):
    """
    :type  nums: List[int], k: int
    :rtype: List[int]
    """
    res = []
    # 统计各个数字出现的次数
    dic = collections.Counter(nums)
    # 生成堆, 由于python中的heapify定义是Min-heap, 需要Max-heap的话需要将val变为负值
    max_heap = [(-val, key) for key, val in dic.items()]
    heapq.heapify(max_heap)
    # 讲出现次数最多的topk元素pop出即可,需要pop出key所以最后为[1]
    for i in range(k):
        res.append(heapq.heappop(max_heap)[1])
    return res




if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    res = topKFrequent(nums,k)
    print(res)


