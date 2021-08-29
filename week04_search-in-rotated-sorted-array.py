def search(nums, target):
    """
    :type: nums: List[int] target: int
    :rtype: n:int
    """

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        # 使用二分法, 查看mid在数组的左半段还是右半段
        # target在左半段
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # target在右半段
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    res = search(nums,target)
    print(res)
