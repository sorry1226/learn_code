def canJump(nums):
    """
    :type: nums: List[int]
    :rtype: n:int
    """
    # m表示能跳到的最远距离
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i + n)
    return True


if __name__ == '__main__':
    nums1 = [2,3,1,1,4]
    nums2 = [3,2,1,0,4]

    res = canJump(nums2)
    print(res)

