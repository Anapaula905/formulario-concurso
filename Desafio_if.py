
print("=" * 40)
print("     INSCRIÇÃO - CONCURSO PÚBLICO")
print("=" * 40)
nome = input("Informe seu nome completo: ")

idade = int(input("Informe sua idade: "))

cpf = input("Informe o seu cpf: ")
while len(cpf) != 11:
    print("CPF inválido. O CPF deve possuir 11 caracteres.")
    cpf = input("Digite o CPF novamente: ")
else:
    print("CPF inválido. O CPF deve possuir 11 caracteres")
    cpf_valido = True

#Verificação de Idade
if idade <18:
    print("Inscrição não permitida.O candidato deve ter 18 anos ou mais")
    exit()
else:
    print("Idade permitida.")

#Escolaridade
escolaridade = int(input(""" \nEscolha a sua escolaridade:
1 - Ensino Médio
2 - Ensino Superior
3 - Pós-graduação
Digite sua opção: """))

while escolaridade < 1 or escolaridade > 3:
    print("Opção inválida! Escolha 1, 2 ou 3.")
    escolaridade = int(input("Digite sua opção novamente: "))

if escolaridade == 1:
    escolaridade_nome = 'Ensino Médio'
elif escolaridade == 2:
    escolaridade_nome = 'Ensino Superior'
elif escolaridade == 3:
    escolaridade_nome = 'Pós-graduação'
else: escolaridade_nome = 'Inválida'

#Sexo
sexo = input("\nInforme o seu sexo(M/F):").upper()
if sexo == "M":
 documento = 'Certificado de Reservista'
elif sexo == "F":
 documento = "Não necessita de documento militar"
else: documento = "Informação inválida"


# Área profissional
area = int(input("""\nEscolha a área desejada:
1 - Administração
2 - Tecnologia da Informação
3 - Educação
Digite sua opção: """))

while area < 1 or area > 3:
    print("Opção inválida! Escolha 1, 2 ou 3.")
    area = int(input("Digite sua opção novamente: "))

if area == 1:
    area_nome = "Administração"
    cargo = "Analista Administrativo"

elif area == 2:
    area_nome = "Tecnologia da Informação"
    cargo = "Analista de Sistemas"

elif area == 3:
    area_nome = "Educação"
    cargo = "Professor"

else:
    area_nome = "Inválida"
    cargo = "Não definido"


# Status da Inscrição
if idade < 18:
    status = "INSCRIÇÃO COM PENDÊNCIAS"
elif escolaridade_nome == "Inválida":
    status = "INSCRIÇÃO COM PENDÊNCIAS"
elif sexo != "M" and sexo != "F":
    status = "INSCRIÇÃO COM PENDÊNCIAS"
elif area_nome == "Inválida":
    status = "INSCRIÇÃO COM PENDÊNCIAS"
elif cpf_valido == False:
    status = "INSCRIÇÃO COM PENDÊNCIAS"
else:
    status = "INSCRIÇÃO APROVADA"


print()
print("=" * 40)
print("       RESUMO DA INSCRIÇÃO")
print("=" * 40)

print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"Idade: {idade}")
print(f"Escolaridade: {escolaridade_nome}")
print(f"Área profissional: {area_nome}")
print(f"Cargo: {cargo}")
print(f"Documento adicional: {documento}")
print(f"Status: {status}")

print("=" * 40)
