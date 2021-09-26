
def reverseBits(n):
    """
    :type   n : int
    :rtype: n : int
    """
    # 每次把 res 左移，把 n 的二进制末尾数字，拼接到结果 res 的末尾。然后把 n 右移
    res = 0
    for i in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res

if __name__ == '__main__':
    print(reverseBits(11111101))
