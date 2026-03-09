'''

CRUD

Açai

um aplicativo fast food, onde voce pode pedir sua sobremesa, personalizar o seu açai , efetuar o seu 
pagamento e acompanhar o seu pedido

'''


print('\n== SITE AÇAI===')
print('1. Fazer o pedido')
print('2. Ver meus pedidos ')
print('3.Mudar rapido ')
print('4. Cancelar pedido')
print('5.Relátorio do pedido')
print('6.Sair')

while True:

    escolha_cliente = input('o que voce deseja fazer?')

    if escolha_cliente == '1':
        print('vamos começar o seu pedido')

        nome_cliente = input('Digite seu nome:')
        print('Aqui está o seu cardápio')

        print('1- Açai 300ml (10R$)')
        print('2- Açai 500ml (20R$)')
        print('3 - Açai 1L (30R$)')

        pedido_cliente = input('qual número do cardapio voce gostaria de pedir?:')

        if pedido_cliente == '1':
            print('Voce escolheu o açai de 300ml.')

        elif pedido_cliente == '2':
            print('Voce escolhe o açai de 500ml.')

        elif pedido_cliente == "3":
            print('Voce escolheu o açai de 1 Litro.')

        else:
            print('Voce escolheu uma opção invalida.')    

        forma_pagamento = input('qual será a forma de pagamento?')

        endereco_cliente = input('Nos informe em qual endereço será entregue o pedido:')

        confirmar_endereco = input(f'O endereço: {endereco_cliente} está correto?')

        if confirmar_endereco == 'sim':
            print('seu pedido foi confirmado')
        else:
            print('faça seu pedido novamente.')
        break

    elif escolha_cliente == '2':
        print('Aqui está seus pedidos:')

    elif escolha_cliente == '3':
        mudar_pedido = input('Oque você deseja mudar no seu pedido?')
        confirmar_pedido = input(f'você modificou isto: {mudar_pedido}?')

    elif escolha_cliente == '4':
        cancelar_pedido = input('Voce gostaria de cancelar seu pedido?')
    
        if cancelar_pedido == 'sim':
            print('seu pedido foi cancelado com sucesso!')

        else:
            print('Seu pedido não foi cancelado')

    elif escolha_cliente == '5':
         print('Aqui esta o relátorio do seu pedido!.')

    elif escolha_cliente == '0':
        print('Saindo do site. volte sempre')
        break

    else:
     print('Opção invalida. por favor tente novamente.')