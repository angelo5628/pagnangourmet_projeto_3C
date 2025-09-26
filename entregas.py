ultimo_id = 0
id_entrega = ultimo_id + 1

cliente_id = int(input("ID do cliente: "))
endereco = input("Endereço: ")
valor_total = float(input("Valor total R$ "))
taxa = float(input("Taxa de entrega R$ "))

print(f"\nID: {id_entrega}")
print(f"ID Cliente: {cliente_id}")
print(f"Endereço: {endereco}")
print(f"Valor total: R$ {valor_total:.2f}")
print(f"Taxa: R$ {taxa:.2f}")
print(f"Status: preparando")
