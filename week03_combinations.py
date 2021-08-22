from itertools import combinations

# 方法1用python自带的combinations方法
def combine1(n, k):
    """
    :type n: int, k: int
    :rtype: List[List[int]]
    """
    return list(combinations(range(1, n + 1), k))

# 方法2找到国外某大神的解法, 没太看懂..先把答案记下来
def combine2(n, k):
    if k == 0:
        return [[]]
    return [pre + [i] for i in range(k, n + 1) for pre in combine2(i - 1, k - 1)]


if __name__ == '__main__':
    res = combine2(4, 2)
    print(res)
