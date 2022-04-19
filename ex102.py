def factorial(n, show=False):
    """
     -> Calculate the Factorial of a number.
     :param n: The number to calculate.
     :param show: (optional) Whether or not to show the account.
     :return: The Factorial value of a number n.
     """
    print('-' * 30)
    result = 0
    for c in range(n, 1, -1):
        if c == n:
            result = n
        c -= 1
        result *= c
    if show is True:
        print(f'{n} x ', end='')
        for c in range(n - 1, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
                break
            print(f'{c} x ', end='')
    return result


print(factorial(5, show=True))
help(factorial)
