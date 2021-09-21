def climbStairs(n):


    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(2, n):
        a, b = b, a + b
    return b


if __name__ == '__main__':

    print(climbStairs(5))

