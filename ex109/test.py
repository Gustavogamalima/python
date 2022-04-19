from ex109 import coin

value = float(input('Enter price: R$'))
print(f'The half of {coin.coin(value)} is {coin.half(value, conversion=False)}')
print(f'The double of {coin.coin(value)} is {coin.double(value, conversion=True)}')
print(f'Increasing it by 10%, we get {coin.increase(value, 10, True)}')
print(f'Reducing 13%, we have {coin.toDecrease(value, 13, True)}')
