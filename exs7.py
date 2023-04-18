with open('names.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

    contagem_nomes = {}

    for linha in linhas:
        nome = linha.strip()

        if nome not in contagem_nomes:
            contagem_nomes[nome] = 0

        contagem_nomes[nome] += 1

    for nome, contagem in contagem_nomes.items():
        print(nome + ': ' + str(contagem))