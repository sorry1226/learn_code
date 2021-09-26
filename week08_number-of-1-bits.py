

def hammingWeight1(n):
    """
    :type  n : int
    :rtype: n : int
    """
    return bin(n).count('1')


def hammingWeight2(n):
    """
    :type  n : int
    :rtype: n : int
    """
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res

if __name__ == '__main__':
    print(hammingWeight1(3))
