# teste de calculadora simples em python
def calculadora():
    As = str(input('''digite (numero) (sinal) (numero)
+ para adição
- para subtração
/ para divisão
* para multiplicação
'''))
    B = As.split()
    C = float(B[0])
    D = (B[1])
    E = float(B[2])
    if D == '+':
        print('\n{} + {} ='.format(C, E))
        print(C+E)
    elif D == '-':
        print('\n{} - {} ='.format(C, E))
        print(C-E)
    elif D == '*':
        print('\n{} * {} ='.format(C, E))
        print(C*E)
# necessario adicionar metodo para divisão por 0 ser igual a nulo
    elif D == '/':
        print('\n{} / {} ='.format(C, E))
        print(C/E)
    else:
        print('operação invalida')
    repetir()


def repetir():
    denovo = input('''
Deseja realizar outro calculo?
S para sim, N para não
    ''')
    if denovo.upper() == 'S':
        calculadora()
    elif denovo.upper() == 'N':
        print('Até mais!')
    else:
        repetir()


calculadora()
