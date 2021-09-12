def longestValidParentheses(s):
    """
    :type: s:str
    :rtype: n:int
    """
    # 我们用 dp[i] 表示以 i 结尾的最长有效括号；
    # 当 s[i] 为 (,dp[i] 必然等于 0，因为不可能组成有效的括号；
    # 那么 s[i] 为 )
    # 1) 当 s[i-1] 为 (，那么 dp[i] = dp[i-2] + 2；
    # 2) 当 s[i-1] 为 ) 并且 s[i-dp[i-1] - 1] 为 (，那么 dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]；

    if len(s) < 1:
        return 0
    dp = [0] * len(s)
    res = 0
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            elif i-dp[i-1]-1 >= 0 and s[i - dp[i - 1] -1] == '(':
                dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
            res = max(res,dp[i])

    return res


if __name__ == '__main__':
    s = ")()())"
    print(longestValidParentheses(s))
