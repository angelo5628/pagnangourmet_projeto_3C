ultimo_id = 0
id_avaliacao = ultimo_id + 1

comanda_id = int(input("ID da comanda: "))

nota_valida = False
while not nota_valida:
    nota = int(input("Nota (1-5): "))
    if 1 <= nota <= 5:
        nota_valida = True
    else:
        print("Nota deve ser entre 1 e 5.")

comentario = input("Comentário: ")

print(f"\nID: {id_avaliacao}")
print(f"ID Comanda: {comanda_id}")
print(f"Nota: {nota}")
print(f"Comentário: {comentario}")
