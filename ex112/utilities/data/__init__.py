
def readMoney(text):
    while True:
        result = str(input(text)).strip().replace(',', '.')
        if result.replace('.', '', 1).isdigit():
            result = float(result)
            return result
            break
        else:
            print(f'\033[1;31mERROR: "{result}" is an invalid price!\033[0;0m')

