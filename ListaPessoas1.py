def add_pessoas():
    nome = str(input('Digite o nome: '))
    idade = input('Digite a idade: ')
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}, {idade}\n')
    print('Pessoa adicionada! ')


def listar_pessoas():
    print('Lista de todas as pessoas: ')
    with open('pessoas.txt', 'r') as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(',')
            print(f'Nome: {nome}, Idade: {idade}')
    print('Lista finalizada! ')


def mudar_info():
    nome_antigo = input(
        'Digite o nome da pessoa que você deseja alterar os dados: ')
    with open('pessoas.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    for i, linha in enumerate(linhas):
        nome, idade = linha.strip().split(',')
        if nome == nome_antigo:
            nome_novo = str(input('Digite o novo nome: '))
            idade_nova = input('Digite a nova idade: ')
            linhas[i] = f'{nome_novo}, {idade_nova}\n'
            with open('pessoas.txt', 'w') as arquivo:
                arquivo.writelines(linhas)
            print('Dados alterados! ')
