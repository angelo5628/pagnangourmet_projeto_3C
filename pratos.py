ultimo_id = 0
id_prato = ultimo_id + 1

nome = input("Nome do prato: ")
descricao = input("Descrição: ")
preco = float(input("Preço R$ "))
categoria_id = int(input("ID da categoria: "))

print(f"\nID: {id_prato}")
print(f"Nome: {nome}")
print(f"Descrição: {descricao}")
print(f"Preço: R$ {preco:.2f}")
print(f"ID Categoria: {categoria_id}")
