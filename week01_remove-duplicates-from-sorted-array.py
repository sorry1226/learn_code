
def removeDuplicates(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j + 1






if __name__ == '__main__':
    nums = [1,1,2,2,3,5]
    n = removeDuplicates(nums)
    print(n)