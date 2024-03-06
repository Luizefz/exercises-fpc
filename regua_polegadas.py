def criar_regua(polegadas, altura):
    if polegadas < 1:
        return
    else:
        # Imprime a marcação atual, apenas se polegadas for diferente de 0
        if polegadas != 0:
            print(f'{polegadas} {"-" * altura}')
        # Chama a função recursivamente com metade das polegadas e da altura
        criar_regua(polegadas // 2, altura + 1)
        print(f'{polegadas} {"-" * altura}')
        criar_regua(polegadas // 2, altura + 1)

# Teste
polegadas = 16
altura = 3

print("Régua:")
criar_regua(polegadas, altura)
