def vote(b):
    from datetime import datetime
    age = datetime.now().year - b
    if age < 16:
        return f'Com {age} anos: NÃO VOTA.'
    elif age < 18 or age >= 65:
        return f'Com {age} anos: VOTO OPCIONAL.'
    else:
        return f'Com {age} anos: VOTO OBRIGATÓRIO.'


print('-' * 30)
print(vote(int(input('Em que ano você nasceu? '))))
