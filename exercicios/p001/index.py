import time
e = ''


def menu():
    print('-=' * 10, 'Menu principal de conversões', '-=' * 10)
    print('[1] - Moeda')
    print('[2] - Temperatura')
    print('[3] - Tempo')
    print('[4] - Fechar menu')
    print('-=' * 30)


def moeda():
    print('-=' * 10, 'Opções', '-=' * 10)
    print('[1] - De Eur para Real')
    print('[2] - De Real para Eur')
    print('[3] - De Eur para Dólar')
    print('[4] - De Dólar para Eur')
    print('[5] - De Dólar para Real')
    print('[6] - De Real para Dólar')
    print('[7] - Voltar ao menu principal')
    print('-=' * 30)
    em = ''
    while True:
        try:
            em = int(input('Digite a sua escolha: '))
            break
        except:
            print('\033[31mErro!!\033[0;0m')
    while em > 7 or em < 1:
        print('\033[31mDigite uma opção válida!!\033[0;0m')
        while True:
            try:
                em = int(input('Digite a sua escolha: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
    if em == 1:
        while True:
            try:
                valor_euro_1 = float(input('Digite o valor em euros: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadom1 = valor_euro_1 * 5.37
        print(f'O resultado da conversão é {resultadom1} reais')
    elif em == 2:
        while True:
            try:
                valor_real_2 = float(input('Digite o valor em reais: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadom2 = valor_real_2 / 5.37
        print(f'O resultado da conversão é {resultadom2}')
    elif em == 3:
        while True:
            try:
                valor_euro_3 = float(input('Digite o valor em euros: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadom3 = valor_euro_3 * 1.07
        print(f'O resultado da conversão é {resultadom3} dólares')
    elif em == 4:
        while True:
            try:
                valor_dolar_1 = float(input('Digite o valor em dólares: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadom4 = valor_dolar_1 / 1.07
        print(f'O resultado da conversão é {resultadom4} euros')
    elif em == 5:
        while True:
            try:
                valor_dolar_2 = float(input('Digite o valor em dólares: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadom5 = valor_dolar_2 * 5.01
        print(f'O resultado da conversão foi {resultadom5} reais')
    elif em == 6:
        while True:
            try:
                valor_real_3 = float(input('Digite o valor em reais: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadom6 = valor_real_3 / 5.01
        print(f'O resultado da conversão é {resultadom6} dólares')


def temperatura():
    print('-=' * 10, 'Opções', '-=' * 10)
    print('[1] - De Celsius para Fahrenheit')
    print('[2] - De Celsius para Kelvin')
    print('[3] - De Fahrenheit para Celsius')
    print('[4] - De Fahrenheit para Kelvin')
    print('[5] - De Kelvin para Fahrenheit')
    print('[6] - De Kelvin para Celsius')
    print('[7] - Voltar ao menu principal')
    print('-=' * 30)
    et = ''
    while True:
        try:
            et = int(input('Digite a sua escolha: '))
            break
        except:
            print('\033[31mErro!!\033[0;0m')
    while et < 1 or et > 7:
        print('\033[31mDigite uma opção válida!!\033[0;0m')
        while True:
            try:
                et = int(input('Digite a sua escolha: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
    if et == 1:
        while True:
            try:
                valor_celsius_1 = float(input('Digite o valor em graus Celsius: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadot1 = (valor_celsius_1 * 1.8) + 32
        print(f'O resultado da conversão é {resultadot1} graus Fahrenheit')
    elif et == 2:
        while True:
            try:
                valor_celsius_2 = float(input('Digite o valor em graus Celsius: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadot2 = valor_celsius_2 + 273.15
        print(f'O resultado da conversão é {resultadot2} graus Kelvin')
    elif et == 3:
        while True:
            try:
                valor_fahrenheit_1 = float(input('Digite o valor em graus Fahrenheit: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadot3 = (valor_fahrenheit_1 - 32) / 1.8
        print(f'O resultado da conversão é {resultadot3} graus Celsius')
    elif et == 4:
        while True:
            try:
                valor_fahrenheit_2 = float(input('Digite o valor em graus Fahrenheit: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadot4 = (valor_fahrenheit_2 - 32) / 1.8 + 273.25
        print(f'O resultado da conversão é {resultadot4} graus Kelvin')
    elif et == 5:
        while True:
            try:
                valor_kelvin_1 = float(input('Digite o valor em graus Kelvin: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadot5 = (valor_kelvin_1 - 273.15) * 1.8 + 32
        print(f'O resultado da conversão é {resultadot5} graus Fahrenheit')
    elif et == 6:
        while True:
            try:
                valor_kelvin_2 = float(input('Digite o valor em graus kelvin: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadot6 = valor_kelvin_2 - 273.15
        print(f'O resultado da conversão é {resultadot6} graus Celsius')


def tempo():
    print('-=' * 10, 'Opções', '-=' * 10)
    print('[1] - De Segundos para Minutos')
    print('[2] - De Segundos para Horas')
    print('[3] - De Minutos para Segundos')
    print('[4] - De Minutos para Horas')
    print('[5] - De Horas para Segundos')
    print('[6] - De Horas para Minutos')
    print('[7] - Voltar ao menu principal')
    print('-=' * 30)
    eti = ''
    while True:
        try:
            eti = int(input('Digite a sua escolha: '))
            break
        except:
            print('\033[31mErro!!\033[0;0m')
    while eti < 1 or eti > 7:
        print('\033[31mDigite uma opção válida!!\033[0;0m')
        while True:
            try:
                eti = int(input('Digite a sua escolha: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
    if eti == 1:
        while True:
            try:
                valor_segundos_1 = float(input('Digite o valor em segundos: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadoti1 = valor_segundos_1 * 0.0167
        print(f'O resultado da conversão é {resultadoti1} minutos')
    elif eti == 2:
        while True:
            try:
                valor_segundos_2 = float(input('Digite o valor em segundos: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadoti2 = valor_segundos_2 / 3600
        print(f'O resultado da conversão é {resultadoti2} horas')
    elif eti == 3:
        while True:
            try:
                valor_minutos_1 = float(input('Digite o valor em minutos: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadoti3 = valor_minutos_1 * 60
        print(f'O resultado da conversão é {resultadoti3} segundos')
    elif eti == 4:
        while True:
            try:
                valor_minutos_2 = float(input('Digite o valor em minutos: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadoti4 = valor_minutos_2 * 0.0167
        print(f'O resultado da conversão é {resultadoti4} horas')
    elif eti == 5:
        while True:
            try:
                valor_horas_1 = float(input('Digite o valor em horas: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadoti5 = valor_horas_1 * 3600
        print(f'O resultado da conversão é {resultadoti5} segundos')
    elif eti == 6:
        while True:
            try:
                valor_horas_2 = float(input('Digite o valor em horas: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
        resultadoti6 = valor_horas_2 * 60
        print(f'O resultado da conversão é {resultadoti6} minutos')


while True:
    menu()
    while True:
        try:
            e = int(input('Digite a sua escolha: '))
            break
        except:
            print('\033[31mErro!!\033[0;0m')
    while e < 1 or e > 4:
        print('\033[31mDigite uma opção válida!!\033[0;0m')
        while True:
            try:
                e = int(input('Digite a sua escolha: '))
                break
            except:
                print('\033[31mErro!!\033[0;0m')
    if e == 4:
        print('Fechando o programa....')
        time.sleep(1)
        break
    if e == 1:
        moeda()
    if e == 2:
        temperatura()
    if e == 3:
        tempo()
