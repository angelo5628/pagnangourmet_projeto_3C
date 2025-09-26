ultimo_id = 0
id_fornecedor = ultimo_id + 1

nome = input("Nome do fornecedor: ")
contato = input("Nome do contato: ")

telefone_valido = False
while not telefone_valido:
    telefone = input("Telefone (com DDD): ")
    if len(telefone) in [10, 11] and telefone.isdigit():
        telefone_valido = True
    else:
        print("Telefone inválido.")

if len(telefone) == 10:
    telefone_formatado = f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
else:
    telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"

tipo = input("Tipo do produto: ")

print(f"\nID: {id_fornecedor}")
print(f"Nome: {nome}")
print(f"Contato: {contato}")
print(f"Telefone: {telefone_formatado}")
print(f"Tipo: {tipo}")
