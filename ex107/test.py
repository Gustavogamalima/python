from ex108 import coin

value = float(input('Enter price: R$'))
print(f'The half of {coin.coin(value)} is {coin.coin(coin.half(value))}')
print(f'The double of {coin.coin(value)} is {coin.coin(coin.double(value))}')
print(f'Increasing it by 10%, we get {coin.coin(coin.increase(value, 10))}')
print(f'Reducing 13%, we have {coin.coin(coin.toDecrease(value, 13))}')
