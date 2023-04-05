def add_pessoas():
    nome = str(input('Digite o nome: '))
    idade = input('Digite a idade: ')
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}, {idade}\n')
    print('Pessoa adicionada! ')

def listar_pessoas():
    print('Lista de todas as pessoas: ')
    with open ('pessoas.txt' , 'r') as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(',')
            print(f'Nome: {nome}, Idade: {idade}')
    print('Lista finalizada! ')

def mudar_info():
    nome_antigo = input('Digite o nome da pessoa que você deseja alterar os dados: ')
    with open ('pessoas.txt' , 'r') as arquivo:
        linhas = arquivo.readlines()
    for i, linha in enumerate(linhas):
        nome, idade = linha.strip().split(',')
        if nome == nome_antigo:
            nome_novo = str(input('Digite o novo nome: '))
            idade_nova = input('Digite a nova idade: ')
            linhas[i] = f'{nome_novo}, {idade_nova}\n'
            with open('pessoas.txt' , 'w') as arquivo:
                arquivo.writelines(linhas)
            print('Dados alterados! ')


def remover_pessoa():
    nome = str(input('Digite o nome que quer remover: '))
    with open ('pessoas.txt' , 'r') as arquivo:
        linhas = arquivo.readlines()
    for i, linha in enumerate(linhas):
        if nome in linha:
            del linhas[i]
            with open('pessoas.txt', 'w') as arquivo:
                arquivo.writelines(linhas)
            print('Pessoa deletada!')

while True:
    print('\n ========= MENU ============ \n')
    print('0 - Sair')
    print('1 - Adicionar pessoas')
    print('2 - Listar pessoas')
    print('3 - Atualizar informações')
    print('4 - Excluir pessoa')
    print('\n =========================== \n')

    escolha = input('Defina o que deseja fazer: ')

    if escolha == '1':
        add_pessoas()

    elif escolha == '2':
        listar_pessoas()

    elif escolha == '3':
        mudar_info()

    elif escolha == '4':
        remover_pessoa()

    elif escolha == '0':
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida. Tente novamente!')
