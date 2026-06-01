while True:
    print("\n MENU")
    print("1 - Verificar maioridade")
    print("2 - Verificar CPF")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        idade = int(input("Digite sua idade: "))

        if idade >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")

    elif opcao == "2":
        cpf = input("Digite o CPF: ")

        if len(cpf) == 11:
            print("CPF válido em quantidade de dígitos.")
        else:
            print("CPF inválido. Deve conter exatamente 11 dígitos.")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")