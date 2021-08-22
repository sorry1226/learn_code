from functools import reduce


def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    perms = [[]]
    for n in nums:
        perms = [p[:i] + [n] + p[i:]
                 for p in perms
                 for i in range((p + [n]).index(n) + 1)]
    return perms


def permuteUnique2(nums):
    res = []
    nums.sort()
    dfs(nums, [], res)
    return res

def dfs(nums, path, res):
    if not nums:
        res.append(path)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


if __name__ == '__main__':
    res = permuteUnique2([1,1,3])
    print(res)
