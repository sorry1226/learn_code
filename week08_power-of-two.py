
def isPowerOfTwo(n):
    """
    :type  n : int
    :rtype: bool
    """
    # 若 n = 2^x
    #   且 x 为自然数（即 n 为 2 的幂），则一定满足以下条件：
    # 1. 恒有 n & (n - 1) == 0，这是因为：
    #       n 二进制最高位为 1，其余所有位为 0；
    #       n - 1 二进制最高位为 0，其余所有位为 1；
    # 2. 一定满足 n > 0。

    return n > 0 and n & (n - 1) == 0


if __name__ == '__main__':
    print(isPowerOfTwo(2))
