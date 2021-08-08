
def moveZeroes(nums) -> None:

    """
    Do not return anything, modify nums in-place instead.
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j]= nums[i]
            j += 1
    for j in range(j,len(nums)):
        nums[j] = 0





if __name__ == '__main__':
    nums = [1,0,3,0,5,0,6,8,0]
    moveZeroes(nums)
    print(nums)

