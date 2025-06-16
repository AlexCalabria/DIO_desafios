saldo = 3000
limite_saque = 600
# Variáveis de controle
print ('\nBem-vindo ao banco!')
    
opcao = int(input('Escolha uma opção:\n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair \n '))
while True:
    if opcao == 1:
        saque = float(input('Qual o valor do saque? '))
        if saque <= saldo and saque <= limite_saque:
            print ('Saque realizado!')
            saldo -= saque
            print ('Saldo atual: ', saldo)


        elif saque <= saldo and saque > limite_saque:
            print ('Saque excede o limite de saque!')
            print ('Limite de saque: ', limite_saque)
   
        else:
            print ('Saldo insuficiente!')
            print ('Saldo atual: ', saldo)

    elif opcao == 2:
        deposito = float( input ('Qual o valor a ser depositado? '))

        if deposito > 0:
            print ('Depósito realizado!')
            saldo += deposito
            print ('Saldo atual: ', saldo)
    
        else: 
            print ('Valor inválido!')
            print ('Valor do depósito: ', deposito)

    elif opcao == 3:
        print ('Extrato: ')
        print ('Saldo atual: ', saldo)

    elif opcao == 4:
        print ('Obrigado por usar nosso banco!')    
        print ('Saindo...')
        print ('Até logo!')
        
    else:
        print ('Opção inválida!')
        print ('Escolha uma opção válida!') 
        
    opcao = int(input('Escolha uma opção:\n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair \n '))
    if opcao == 4:
        break
print ('Obrigado por usar nosso banco!')    
print ('Saindo...')
print ('Até logo!') 


