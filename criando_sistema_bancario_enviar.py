exibir_menu = """ \n
    =======Menu=======
    [1] - \tDepositar
    [2] - \tSacar  
    [3] - \tExtrato
    [4] - \tSair
    =>"""
    
saldo = 500
extrato = ""
numero_saque = 0 
LIMITE_QUANTIDADE_SAQUE = 3
LIMITE_SAQUE = 500

while True:
    opcao = input(exibir_menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso!")
            extrato += f"\n Depósito no valor de R$ {valor:.2f}" #verificar necessidade de quebrar linha
        
        else: print("Valor inválido, tente novamente!")


    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        saldo_insuficiente = valor > saldo #valores boleanos porque retorna em False and true.
        #uso parenteses apenas com funções e métodos.
        
        limite_saque_excedido = valor > LIMITE_SAQUE

        quantidade_saque_excedida = numero_saque >= LIMITE_QUANTIDADE_SAQUE

        if saldo_insuficiente:   #neste caso não coloco parenteses antes dos dois pontos, porque apenas funções e objetos chamáveis pode-se adicionar.
            print("Saldo insuficiente! Por favor, tente outro valor.")
#elif diz que se não for a primeira opção será a segunda, enquanto que if vai ficar testando todas as opões, então se atender a duas opções as duas serão exibidas na saída
#neste caso quero que apenas uma seja, então coloco elif ao invés de if.
        elif limite_saque_excedido:
            print("O valor solicitado é maior do que o limite de saque. Por favor tente outro valor.")

        elif quantidade_saque_excedida:
            print("Você excedeu a quantidade de saque diário." \
            "Tente novamente amanhã.")
        
        elif valor > 0:
            saldo -= valor 
            print("Saque realizado com sucesso!")
            extrato += f"\n Saque no valor de R$ {valor:.2f}"
            numero_saque += 1
        
        else: 
            print("Valor inválido. Digite um valor válido.")


    elif opcao == "3":
        print("=======EXTRATO=======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n saldo: R$ {saldo: .2f}")
        print("=====================")
    
    elif opcao == "4":
        break

    else:
        print("Operação inválida! Tente novamente.")
