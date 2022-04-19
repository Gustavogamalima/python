from time import sleep


def write(phrase, color='without color'):
    if color == 'red':
        color = '\033[1;97;41m'
    elif color == 'green':
        color = '\033[1;97;42m'
    elif color == 'yellow':
        color = '\033[1;97;43m'
    elif color == 'blue':
        color = '\033[1;97;44m'
    elif color == 'without color':
        color = '\033[0;0m'
    print(f'{color}~' * (len(phrase) + 4))
    print(f'  {phrase}')
    print('~' * (len(phrase) + 4))
    print(f'\033[0;0m', end='')


def pyhelpHelpSystem():
    while True:
        write('PyHELP HELP SYSTEM', 'green')
        functionOrLibrary = str(input('Function or Library > ')).strip().lower()
        if functionOrLibrary == 'end':
            write('SEE YOU LATER!', 'red')
            break
        write(f"Accessing command manual '{functionOrLibrary}'", 'blue')
        sleep(0.5)
        print('\033[1;30;107m', end='')
        help(functionOrLibrary)
        print(f'\033[0;0m', end='')
        sleep(0.5)


pyhelpHelpSystem()
