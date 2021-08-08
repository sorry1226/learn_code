
def rotate(nums, k) -> None:

    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[: -k]
    # def numReverse(start, end):
    #     while start < end:
    #         nums[start], nums[end] = nums[end], nums[start]
    #         start += 1
    #         end -= 1
    #
    # k, n = k % len(nums), len(nums)
    # if k:
    #     numReverse(0, n - 1)
    #     numReverse(0, k - 1)
    #     numReverse(k, n - 1)




if __name__ == '__main__':
    nums = [1,3,5,7,9,0,3]
    k = 3
    rotate(nums,3)
    print(nums)
