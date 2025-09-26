ultimo_id = 0
id_cliente = ultimo_id + 1

nome = input("Nome completo: ")

telefone_valido = False
while not telefone_valido:
    telefone = input("Telefone: ")
    if len(telefone) in [10, 11] and telefone.isdigit():
        telefone_valido = True
    else:
        print("Telefone inválido.")

if len(telefone) == 10:
    telefone_formatado = f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
else:
    telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"

email = input("E-mail: ")

print(f"\nID: {id_cliente}")
print(f"Nome: {nome}")
print(f"Telefone: {telefone_formatado}")
print(f"E-mail: {email}")
