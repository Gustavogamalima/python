expression = []
openSquareBrackets = closeBrackets = 0
expression = [str(input('Digite a expressão: ')).strip()]
for value in expression:
    if value == '(':
        openSquareBrackets += 1
    if value == ')':
        closeBrackets += 1
if openSquareBrackets == closeBrackets:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
