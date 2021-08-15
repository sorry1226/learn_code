import heapq


def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """

    # 通过小根堆实现
    #
    # 每次取出堆顶元素 xx，则 xx 是堆中最小的丑数，由于 2x, 3x, 5x2x,3x,5x 也是丑数，因此将 2x, 3x, 5x2x,3x,5x 加入堆。
    #
    # 上述做法会导致堆中出现重复元素的情况。为了避免重复元素，可以使用哈希集合去重，避免相同元素多次加入堆。
    # 首先将最小的丑数 1 加入堆。
    heap = [1]
    visited = set([1])

    for i in range(n - 1):
        val = heapq.heappop(heap)
        # 每次取出堆顶元素 xx，则 xx 是堆中最小的丑数，由于 2x, 3x, 5x2x,3x,5x 也是丑数，因此将 2x, 3x, 5x2x,3x,5x 加入堆。
        for factor in [2, 3, 5]:
            nxt = val * factor
            if nxt not in visited:
                heapq.heappush(heap, nxt)
                visited.add(nxt)
    # 在排除重复元素的情况下，第 n 次从最小堆中取出的元素即为第n个丑数。
    return heapq.heappop(heap)
