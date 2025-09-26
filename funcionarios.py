ultimo_id = 0
id_funcionario = ultimo_id + 1

nome = input("Nome completo: ")

cpf_valido = False
while not cpf_valido:
    cpf = input("CPF (11 números): ")
    if len(cpf) == 11 and cpf.isdigit():
        cpf_valido = True
    else:
        print("CPF inválido.")

cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

cargo = input("Cargo: ")
salario = float(input("Salário R$ "))

print(f"\nID: {id_funcionario}")
print(f"Nome: {nome}")
print(f"CPF: {cpf_formatado}")
print(f"Cargo: {cargo}")
print(f"Salário: R$ {salario:.2f}")
