from datetime import datetime

ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    currentDateTime = datetime.now()
    date = currentDateTime.date()
    ano = int(date.strftime("%Y"))
if ano % 4 == 0:
    if ano % 100 != 0:
        print(f'O ano {ano} é BISSEXTO!')
    else:
        print(f'O ano {ano} NÃO é BISSEXTO')
elif ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')

