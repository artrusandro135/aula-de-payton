print("bom dia")

nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))

média = (nota1 + nota2 + nota3) / 3

if média >= 7.0:
    print("Parabéns! Você foi aprovado com média:",média)
else:
    print("Infelizmente, você foi reprovado com média:",média)