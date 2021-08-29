
def maxProfit(prices):
    """
    :type: List[int]
    :rtype: n:int
    """
    # 贪心算法, 只要第二天的价格比第一天高就卖出
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]

    return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    res = maxProfit(prices)
    print(res)
