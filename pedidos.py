ultimo_id = 0
id_pedido = ultimo_id + 1

comanda_id = int(input("ID da comanda: "))
prato_id = int(input("ID do prato: "))
quantidade = int(input("Quantidade: "))
observacoes = input("Observações: ")

print(f"\nID: {id_pedido}")
print(f"ID Comanda: {comanda_id}")
print(f"ID Prato: {prato_id}")
print(f"Quantidade: {quantidade}")
print(f"Status: pendente")
print(f"Observações: {observacoes}")
