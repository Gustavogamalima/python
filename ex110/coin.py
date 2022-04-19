def half(value=0, conversion=False):
    result = value / 2
    if conversion is True:
        result = coin(result)
    return result


def double(value=0, conversion=False):
    result = value * 2
    if conversion is True:
        result = coin(result)
    return result


def increase(value=0, number=0, conversion=False):
    result = value + (value * number) / 100
    if conversion is True:
        result = coin(result)
    return result


def toDecrease(value=0, number=0, conversion=False):
    result = value - (value * number) / 100
    if conversion is True:
        result = coin(result)
    return result


def coin(parameter=0.0, currencyType='R$'):
    return f'{currencyType}{parameter:.2f}'.replace('.', ',')


def abstract(parameter, increment=10, decrement=10):
    print('-' * 30)
    print(f'{"SUMMARY OF VALUE":^30}')
    print('-' * 30)
    print(f'{"Price analyzed:":<20}{coin(parameter)}')
    print(f'{"Double the price:":<20}{double(parameter, True)}')
    print(f'{"Half-price:":<20}{half(parameter, True)}')
    print(f'{increment}{"% increase:":<18}{increase(parameter, increment, True)}')
    print(f'{decrement}{"% reduction:":<18}{increase(parameter, decrement, True)}')
    print('-' * 30)
