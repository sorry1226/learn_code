import collections


def isAnagram1(s: str, t: str):
    dic = {}
    # 遍历字符串1中的所有字母, 放入字典, key为字母值, 初始value为1, 之后字母每出现一次则value +1
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    # 遍历字符串2, 如果字母不在字典则直接返回False, 如果字母在字典则value -1, 如果字符串2为字符串1的异味词, 则最终字典中所有val都为0
    for j in t:
        if j not in dic:
            return False
        else:
            dic[j] -= 1
    # 遍历字典的所有值, 如果出现不为0的value则返回False
    for val in dic.values():
        if val != 0:
            return False
    return True

# 方法2利用collections的Counter依次统计s和t
def isAnagram2(s: str, t: str):

    return collections.Counter(s) == collections.Counter(t)



if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    reuslt1 = isAnagram1(s,t)
    reuslt2 = isAnagram2(s,t)
    print(reuslt1,reuslt2)
