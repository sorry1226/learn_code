def countSubstrings(s):
    """
    :type: s: str
    :rtype: n:int
    """
    # 首先我们构建 dp 数组，dp[i][j] 表示区间范围 [i, j] 的子串是否为回文子串，如果是，则为1，否则为0。
    # 这样递推公式就有两种情况：
    # s[i] != s[j]，那么区间 [i, j] 肯定不是回文子串
    # s[i] == s[j]，就分三种情况来讨论:
    #  1) i = j 是回文串
    #  2) j - i = 1 是回文串
    #  3) j - 1 > 1 则中间部分为回文子串就是, 否则不是

    dp = [[0] * len(s) for _ in range(len(s))]
    res = 0
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = 1
                    res += 1
                elif dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                    res += 1

    return res


if __name__ == '__main__':
    s = "abc"
    print(countSubstrings(s))

