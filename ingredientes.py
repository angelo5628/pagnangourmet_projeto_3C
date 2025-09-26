ultimo_id = 0
id_ingrediente = ultimo_id + 1

nome = input("Nome do ingrediente: ")
unidade = input("Unidade de medida: ")
estoque_atual = float(input("Estoque atual: "))
estoque_minimo = float(input("Estoque mínimo: "))

print(f"\nID: {id_ingrediente}")
print(f"Nome: {nome}")
print(f"Unidade: {unidade}")
print(f"Estoque atual: {estoque_atual}")
print(f"Estoque mínimo: {estoque_minimo}")
