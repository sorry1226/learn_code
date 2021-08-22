import itertools

# 方法1用自带的permutations方法
from functools import reduce


def permute1(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return list(itertools.permutations(nums))


def permute2(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms



def permute3( nums):
    return [[n] + p
            for i, n in enumerate(nums)
            for p in permute3(nums[:i] + nums[i+1:])] or [[]]


def permute4(nums):
    return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                for p in P for i in range(len(p)+1)],
                  nums, [[]])




if __name__ == '__main__':
    res = permute4([1,1,3])
    print(res)
