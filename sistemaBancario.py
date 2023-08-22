menu = "[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair"
saldo = 0
limite = 500
numero_saques = 0
limite_saque = 3

while True:
    print("Saldo atual: R$", saldo)
    print("Número de saques restantes:", limite_saque - numero_saques)
    opcao = input(menu)
    
    if opcao == "d":
        deposito = float(input("Insira o valor que deseja depositar: R$"))
        saldo += deposito
        print("Depósito de R$", deposito, "realizado. Novo saldo: R$", saldo)
        
    elif opcao == "s":
        if numero_saques < limite_saque:
            saque = float(input("Insira o valor que deseja sacar: R$"))
            if saque > saldo:
                print("Saldo insuficiente.")
            elif saque > limite:
                print("Limite de saque por operação excedido.")
            else:
                saldo -= saque
                numero_saques += 1
                print("Saque de R$", saque, "realizado. Novo saldo: R$", saldo)
        else:
            print("Limite diário de saques atingido.")
        
    elif opcao == "e":
        print("Extrato")
        print("Saldo atual: R$", saldo)
        
    elif opcao == "q":
        print("Saindo do sistema.")
        break
    
    else:
        print("Opção inválida, por favor escolha uma opção.")
