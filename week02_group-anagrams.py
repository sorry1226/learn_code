

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic = {}
    # 初始化一个字典,之后依次遍历数组中的字符串并排序, 将排序后的字符串作为key
    # 将key值一样的原字符串放入数组作为value, 之后将字典的value转换为list返回即可
    for str in strs:
        key = ''.join(sorted(str))
        if key not in dic:
            dic[key] = [str]
        else:
            dic[key] += [str]

    return list(dic.values())






if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    reuslt = groupAnagrams(strs)
    print(reuslt)
