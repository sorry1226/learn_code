
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []

    def generate(p, left, right):
        # 因为括号组合组成的字符串长度为2n 所以当最终结果等于2n时返回
        if len(p) == 2 * n:
            res.append(''.join(p))
        # 对于左括号而言如果其个数小于n则可生成
        if left < n:
            p.append('(')
            generate(p, left + 1, right)
            p.pop()
        # 对于有括号而言如果其个数小于左括号而且小于n则可生成 由于上一步左括号一定小于n 所以判断条件可以省略right < n
        if right < left:
            p.append(')')
            generate(p, left, right + 1)
            p.pop()

    generate([], 0, 0)

    return res


if __name__ == '__main__':
    res = generateParenthesis(3)
    print(res)
