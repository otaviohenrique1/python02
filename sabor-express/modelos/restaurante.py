class Restaurante:
    nome = ""
    categoria = ""
    ativo = False
    # ativo: bool = False


restaurante_praca = Restaurante()
# restaurante_praca.nome = "Praça"
# restaurante_praca.categoria = "Gourmet"


restaurante_pizza = Restaurante()


restaurantes = [restaurante_praca, restaurante_pizza]


# print(dir(restaurante_praca))
# print(vars(restaurante_praca))
print(restaurante_praca.ativo)