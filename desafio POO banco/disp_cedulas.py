#funções que contam as cedulas após o saque
def Contar_celulas(valor):
    print("Saque disponiveil: ")
    if valor >= 100:
        if valor % 100 == 0:
            print(f"{valor/100} notas de 100")
            return
        else:
            print(f"{valor//100} notas de 100")
            valor = valor - ((valor//100) * 100)

    if 100 > valor and valor >= 50:
        if valor % 50 == 0:
            print(f"{valor/50} notas de 50")
            return
        else:
            print(f"{valor//50} notas de 50")
            valor = valor - ((valor//50) * 50)

    if 50 > valor and valor >= 20:
        if valor % 20 == 0:
            print(f"{valor/20} notas de 20")
            return
        else:
            print(f"{valor // 20} notas de 20")
            valor = valor - ((valor // 20) * 20)

    if 20 > valor and valor >= 10:
        if valor % 10 == 0:
            print(f"{valor/10} notas de 10")
            return
        else:
            print(f"{valor // 10} notas de 10")
            valor = valor - ((valor // 10) * 10)

    if 10 > valor and valor >= 5:
        if valor % 5 == 0:
            print(f"{valor/5} notas de 5")
            return
        else:
            print(f"{valor // 5} notas de 5")
            valor = valor - ((valor // 5) * 5)

    if 5 > valor and valor >= 2:
        if valor % 2 == 0:
            print(f"{valor/2} notas de 2")
            return
        else:
            print(f"{valor // 2} notas de 2")
            valor = valor - ((valor // 2) * 2)

    if 2 > valor and valor >= 1:
        print("1 nota de 1")
        valor = valor - 1

    print("Saque realizado (não é possivel sacar centavos).")


