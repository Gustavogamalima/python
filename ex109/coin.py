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
