def get_coins(m0):
    """
    function, which returns the minimum number of
    coins needed to pay a given amount of money
    """
    if not isinstance(m0, int):
        raise TypeError
    coins = {}

    q1 = int(m0 / 100)
    m1 = m0 - q1 * 100

    q2 = int(m1 / 50)
    m2 = m1 - q2 * 50

    q3 = int(m2 / 20)
    m3 = m2 - q3 * 20

    q4 = int(m3 / 10)
    m4 = m3 - q4 * 10

    q5 = int(m4 / 5)
    m5 = m4 - q5 * 5

    q6 = int(m5 / 1)

    coins[100] = q1
    coins[50] = q2
    coins[20] = q3
    coins[10] = q4
    coins[5] = q5
    coins[1] = q6

    return coins


def check_palindrome(s):
    """
    Find whether the string is a palindrome
    """
    if not isinstance(s, str):
        raise TypeError
    s = s.lower()
    size = len(s)
    iter : int = size
    # we need to iterate  only half of the string.
    # Pull out the middle char if we have odd number of chars
    for i in range(0, iter):
        if s[i] != s[size - i - 1]:
            return False
    return True
