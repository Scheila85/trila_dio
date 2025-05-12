
def menu():
    exibir_menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar 
    [3]\tExtrato
    [4]\tSaldo
    [5]\tNovo usuário
    [6]\tNova conta
    [7]\tListar contas
    [8]\tSair
    => """
    
    return input(exibir_menu)


def depositar(saldo, valor, extrato, /): 
    if valor > 0:
        saldo += valor 
        extrato += f"Depósito: R${valor:.2f}"  #Estou atribuindo uso +=, -=... se estivesse comparando uso ==, >=... 
        print(f"Depósito no valor de R${valor} realizado com sucesso!")
    else:
        print("Operação falhou, digite um valor válido!")

    return saldo, extrato # peço p retornar só saldo e extrato, porque foram as variáveis que foram modificadas
# com valores sendo adicionados ou retirados delas.

def sacar(*, numero_saques, limite_quantidade_saques, limite_valor_saque, valor, saldo, extrato):
    
    limite_saque_excedido = numero_saques > limite_quantidade_saques
    limite_valor_saque_excedido = valor > limite_valor_saque
    saldo_excedido = valor > saldo

    if saldo_excedido:
        print("Você não possui saldo suficiente, digite outro valor!")
    elif limite_valor_saque_excedido:
        print("Operação falhou. O valor do saque excede o limite.")
    elif limite_saque_excedido:
        print("Operação falhou. Você excedeu o número de saques permitido.")
    
    elif valor <= saldo:
        saldo -= valor
        extrato += f"Saque: R${valor}"  #também uso += porque estou atribuindo e não comparando.
        numero_saques += 1
        print(f"Saque no valor de R${valor} realizado com secesso!")

    else: 
        print("Operação falhou, tente outro valor")
    
    return saldo, extrato 

def exibir_extrato(saldo,/, *, extrato):
    print("=============EXTRATO============")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")
    print("================================")

def exibir_saldo(saldo):
    print(f"saldo: R${saldo}")

    return saldo

def criar_usuario(usuarios):   #posso chamar a função usuarios

    cpf = input("Informe o número do cpf do usuário: ")
    
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("O número de cpf fornecido já está vinculado a um usuário. Se deseja criar uma nova conta \n" \
        "para este usuário, clique na opção (Criar conta)")
        return
    
    nome = input("Informe nome completo: ")
    data_nascimento = input("Informe a data de nascimento do usuário: ")
    endereço = input("Informe endereço completo: rua - bairro - cidade/UF: ")

    usuarios.append({"nome": nome, "CPF": cpf, "data_nascimento": data_nascimento, "endereço": endereço})
    #como chamei usuarios na minha função (como parametro), posso definir meu dicionário aqui
    #caso contrário não conseguiria.
    #Nesse caso, não tem return porque você está apenas adicionando o usuário à 
    #lista usuarios, que está sendo modificada diretamente. 
    #A função (ou script) não precisa devolver nada, porque a lista já foi 
    #alterada e você pode usá-la depois.
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):

    filtrar_usuario = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    # List Comprehension é uma forma de criar uma nova lista com base na filtragem de outra lista.
    # Esse código vai percorrer cada CPF da variável usuários adicionar à variável usuario e criar uma nova
    # lista chamada filtrar_usuario (por isso do usuario antes de for) apenas com a string CPF, se o cpf 
    # digitado for o mesmo que o da lista que o CPF de usuarios, adicionar à variavel filtrar_usuario.
    
    return filtrar_usuario[0] if filtrar_usuario else None
#sempre retorna o primeiro elemento, porque vou achar apenas um usuario porque não posso cadastrar dois
#usuários com o mesmo cpf, se não encontrar retorne none.

def criar_conta_corrente(AGENCIA,usuarios,numero_conta):
    
    cpf = input("Digite o número do seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: 
        print("Conta criada com sucesso!")
#Embaixo RESOLVI o problema de uma conta pertencer somente a um usuário (usuário que eu
# encontrar dependendo do cpf que digitar).
#Porque chaves armazenam apenas um valor. Sempre que eu quiser armazenar apenas
#Um valor sem repetição, uso dicionário.
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
#return: a variável conta só vai receber o dicionario se o usuario existir.
#Usei return porque quero que a função devolva os dados da nova conta.
#Essa informação provavelmente será usada fora da função, por exemplo, 
#para armazenar essa conta ou mostrar ao usuário.
#Use return quando você quiser devolver dados para quem chamou a função.
#Não precisa de return se a função só mudar algo diretamente 
#(como adicionar a uma lista) ou apenas mostrar informações (com print).
    else:
        print("É necessário criar um usuário antes de criar uma conta!")

def listar_contas(AGENCIA, contas, usuario):
    
    contas_listadas = f"""
        Agência: {AGENCIA}
        CC: {contas}
        Usuario: {usuario}"""
    
    print(contas_listadas)

def variaveis():
    LIMITE_QUANTIDADE_SAQUES = 3
    AGENCIA = "0001"

    limite_valor_saque = 500
    saldo = 500
    extrato = " "
    numero_saques = 2
    usuarios =[]  # --> criei a lista usuário e passo a variável para a função criar usuário
    contas =[]

    while True:

        opcao = menu()

        if opcao == "1":

            valor = float(input("Informe o valor do depósito:"))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            
            valor = float(input("Informe o valor do saque:")) #sempre que eu dar um input para digitar um valor
# e esse valor ser adicionado a uma variável, devo coloca-lo como float porque ao ser digitado, será transformado
#para string e vai dar erro, porque string não pode ser somada ou comparado com numeros, por exemplo.
            
            saldo, extrato = sacar(
                numero_saques=numero_saques,
                limite_quantidade_saques=LIMITE_QUANTIDADE_SAQUES,
                limite_valor_saque=limite_valor_saque, 
                valor=valor, 
                saldo=saldo, 
                extrato=extrato)
        
        elif opcao == "3":

            exibir_extrato(saldo, extrato=extrato) 
#não tem saldo e extrato antes de exibir extrato, porque
#nessa função não quero adicionar os valores de saldo e extrato como nas funções de depósito e 
#saque, porque já estou acessando o próprio menu de exibir extrato.       
        elif opcao == "4":
            saldo = exibir_saldo(saldo)

        elif opcao == "5":
        
            criar_usuario(usuarios)  # passei a variável usuários para a função, assim posso chamar ela na
            # função criar usuario
        elif opcao == "6":
            numero_conta = len(contas) + 1
# len + 1 resolve o problema de o número de conta iniciar em 1 e ser sequencial
# vai contar o tanto de itens que tem na linha lista e adicionar mais 1.
            conta = criar_conta_corrente(AGENCIA, usuarios, numero_conta)

            if conta:
                contas.append(conta)
#posso fazer dessa forma ou igual em elif opcao == "5" apenas colocando 
#criar_conta_corrente(AGENCIA,usuarios, contas), ou seja, estaria passando a lista direto.
        elif opcao == "7":
            listar_contas(AGENCIA, contas, usuarios)

        elif opcao == "8": 
            break
        
        else: 
            print("Opção inválida, tente novamente!")
        
variaveis()








