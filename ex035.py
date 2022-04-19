print('-='*30)
print('Analisador de Triângulos')
print('-='*30)
ps = int(input('Primeiro segmento: '))
ss = int(input('Segundo segmento: '))
ts = int(input('Terceiro segmento: '))
if ps + ss > ts and ps + ts > ss and ss + ts > ps:
    print('Os segmentos acima PODEM FORMAR triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')