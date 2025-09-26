ultimo_id = 0
id_restaurante = ultimo_id + 1

nome_restaurante = input("Nome do restaurante: ")

cnpj_valido = False
while not cnpj_valido:
    cnpj = input("CNPJ (14 números): ")
    if len(cnpj) == 14 and cnpj.isdigit():
        cnpj_valido = True
    else:
        print("CNPJ inválido. Use 14 números.")

cnpj_formatado = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

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

endereco = input("Endereço: ")
taxa_entrega = float(input("Taxa de entrega R$ "))

print(f"\nID: {id_restaurante}")
print(f"Nome: {nome_restaurante}")
print(f"CNPJ: {cnpj_formatado}")
print(f"Telefone: {telefone_formatado}")
print(f"Endereço: {endereco}")
print(f"Taxa: R$ {taxa_entrega:.2f}")
