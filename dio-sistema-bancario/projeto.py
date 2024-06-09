menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500 
extrato = []
numeros_saques = 0
limite_saques = 4
contador_saques = 0 
movimentacao = 0 

while True: 

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
    
        saldo += valor

        extrato.append(valor)

        
    elif opcao == "s":
            valor_saque = 0 

            contador_saques += 1 

            if contador_saques >= limite_saques:  
                print("Você atingiu o limite máximo de saques por dia.")

            else: 
                valor_saque = float(input("Informe o valor do saque: "))

          
                if valor_saque > limite:
                    print("O limite do saque é 500, tente novamente")
                else:
                    saldo -= valor_saque
                    extrato.append(('Saque', -valor_saque))
                    print(f"Saque realizado com sucesso. Você fez {contador_saques} saque(s).")


                    
               
    elif opcao == "e":

        if not extrato: 
            print("Não foram realizadas movientações.")

        else:
          for movimentacao in extrato:
                if movimentacao > 0:
                    print("- Depósito: R$ {:.2f}".format(movimentacao))
                else:
                    print("- Saque: R$ {:.2f}".format(-movimentacao))
                print("Saldo atual: R$ {:.2f}".format(saldo))
      
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


   