ps = int(input('Primeiro segmento: '))
ss = int(input('Segundo segmento: '))
ts = int(input('Terceiro segmento: '))
if ps + ss <= ts or ps + ts <= ss or ss + ts <= ps:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
else:
    if ps == ss and ps == ts and ss == ts:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif ps != ss and ps != ts and ss != ts:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')