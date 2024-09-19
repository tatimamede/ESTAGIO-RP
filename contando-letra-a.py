def contar_letra_a(texto):
    # Convertendo o texto para minúsculas para verificar 'a' e 'A'
    texto = texto.lower()
    
    # Contando a ocorrência da letra 'a'
    quantidade_a = texto.count('a')
    
    # Verificando se a letra 'a' existe
    if quantidade_a > 0:
    
        print (f"A letra 'a' (maiúscula ou minúscula) aparece {quantidade_a} vez(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")

# Exemplo de uso
texto = input("Digite uma string: ")
contar_letra_a(texto)
