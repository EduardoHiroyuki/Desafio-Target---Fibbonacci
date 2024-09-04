def contar_as(texto):
    return texto.lower().count('a')

texto = input("Digite um texto: ")
qtd_as = contar_as(texto)
print(f"A letra 'a' aparece {qtd_as} vezes no texto.")