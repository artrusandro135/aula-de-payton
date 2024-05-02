#Verificador de idade criança
print("bom dia tudo bem com vc")

numero_de_pessoas = int(input("Digite o numero de pessoas: "))
media = 0

for i in range(1, numero_de_pessoas + 1):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    media = ((media * (i - 1)) + idade) / i

if media < 26:
    print("A turma é jovem")
elif media < 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")