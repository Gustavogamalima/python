def half(value=0):
    result = value / 2
    return result


def double(value=0):
    result = value * 2
    return result


def increase(value=0, number=0):
    result = value + (value * number) / 100
    return result


def toDecrease(value=0, number=0):
    result = value - (value * number) / 100
    return result


def coin(parameter=0, currencyType='R$'):
    return f'{currencyType}{parameter:.2f}'.replace('.', ',')
