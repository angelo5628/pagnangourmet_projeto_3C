ultimo_id = 0
id_compra = ultimo_id + 1

fornecedor_id = int(input("ID do fornecedor: "))

data_valida = False
while not data_valida:
    data = input("Data (AAAA-MM-DD): ")
    if len(data) == 10 and data[4] == '-' and data[7] == '-':
        data_valida = True
    else:
        print("Data inválida.")

valor_total = float(input("Valor total R$ "))

print(f"\nID: {id_compra}")
print(f"ID Fornecedor: {fornecedor_id}")
print(f"Data: {data}")
print(f"Valor: R$ {valor_total:.2f}")
print(f"Status: pendente")
