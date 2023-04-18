import string
import random

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = ''.join(random.choice(caracteres) for i in range(tamanho))

    return senha

entrada = input("escreva um tamanho de senha: ")
senha = gerar_senha(int(entrada))

print(senha)