print('Select a option')

# if user select 1, print hello, if user select 2, print goodbye

print('1. Iniciar Jogo')
print('2. Sair')
print('3. Créditos')

option = input('Enter a number: ')

while True:
    print('MENU')

    print('1. Iniciar Jogo')
    print('2. Sair')
    print('3. Créditos')

    option = input('Enter a number: ')

    if (option == '1'):
        print('Sucesso!')
    elif (option == '2'):
        print('Bye!')
        break
    elif (option == '3'):
        print('Allan Narok\nDaniel Kondlatsch')
    else:
        print('Opção Inválida')
        break
