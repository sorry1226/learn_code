
def reverseWords(s):
    """
    :type  s : str
    :rtype: str
    """

    return " ".join(reversed(s.split()))




if __name__ == '__main__':
    s = 'one world one dream'
    print(reverseWords(s))
