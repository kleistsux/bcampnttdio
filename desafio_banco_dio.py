menu = """
__________________________________
|||||||||| Banco da Dio ||||||||||


[d] - Depositar
[s] - Sacar
[e] - Extrato

[q] - Sair

__________________________________
 
"""
saldo = 0
qtd_saques = 0
extrato = ""
LIMITE_VALOR_SAQUE = 500
LIMITE_QTD_SAQUE = 3


while True:

    opcao = input(menu)
      
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("A operação falhou! O valor informado não é válido.")
         
    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))

        acima_saldo = valor > saldo
        acima_limite = valor > LIMITE_VALOR_SAQUE
        acima_saque = qtd_saques >= LIMITE_QTD_SAQUE

        if acima_saldo:
            print("A operação falhou! Saldo insulficiente!")

        elif acima_limite:
            print("A operação falhou! O Valor solicitado ultrapassa o limite por saque permitido!")

        elif acima_saque:
            print("A operação falhou! Limite de saque diário atingido!")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qtd_saques += 1
        else:
            print("A operação falhou! O valor informado não é válido.")
        
    elif opcao == "e":
        print("")
        print("")
        print("|||||||||||||| Extrato  Dio ||||||||||||||")
        print("")
        print("Não foram realizadas movimentações até o momento." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("")
        print("==========================================")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada. ")







 