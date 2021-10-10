
def isIsomorphic1(s,t):
    """
    :type  s : str, t : str
    :rtype: bool
    """

    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

def isIsomorphic2(s, t):
    return [s.find(i) for i in s] == [t.find(j) for j in t]



if __name__ == '__main__':
    s = 'hhd'
    t = 'ppd'
    print(isIsomorphic1(s,t))
