def numDecodings(s):
    """
    :type: s: str
    :rtype: n:int
    """

    if not s:
        return 0
    dp = [0 for x in range(len(s) + 1)]

    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2,len(s) + 1):
        # 使用一个字符
        if 0 < int(s[i-1]) <= 9:
             dp[i] += dp[i - 1]
    # 使用两个字符
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[len(s)]


if __name__ == '__main__':
    print(numDecodings(s))

