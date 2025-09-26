ultimo_id = 0
id_pagamento = ultimo_id + 1

comanda_id = int(input("ID da comanda: "))
valor = float(input("Valor R$ "))
metodo = input("Método (dinheiro/cartao/pix): ")

print(f"\nID: {id_pagamento}")
print(f"ID Comanda: {comanda_id}")
print(f"Valor: R$ {valor:.2f}")
print(f"Método: {metodo}")
