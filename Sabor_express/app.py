import os
restaurantes = [{'nome':'Cantina','categoria':'Italiana', 'ativo': False},
                 {'nome':'Japacama', 'categoria':'Japonesa', 'ativo':False},
                 {'nome':'Churras do migUel', 'categoria':'Churrascaria', 'ativo':False} 
]

#Funções estruturais do main()
def exibir_nome_do_programa():
    print("""
   Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
    """)

def mostrar_opcoes():
    print('1. Cadastrar restaurante ')
    print('2. Listar restaurante ')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def escolher_opcao():
    try:
        valor_opcao =  int(input('Escolha uma opção:'))
        if valor_opcao == 1:
            cadastrar_restaurante()
        elif valor_opcao == 2:
            listando_restaurantes()
        elif valor_opcao == 3:
            alternar_status()
        elif valor_opcao == 4:
            finalizar_app()
        else: 
           opcao_invalida()
    except:
        opcao_invalida()

#Funções definidas para as opções do menu principal
def voltar_menu():
    '''Esta função volta para o menu principal'''
    input('\ndigite qualquer tecla para voltar ao menu principal: ')
    main()

def alternar_status():
    '''Esta função altera o status de um restaurante'''
    exibir_subtitulo('Alterar status')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso!!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado!')
            
    
    voltar_menu()
def exibir_subtitulo(texto):
    '''Essa função é utilizada para limpar o sistema e apresentar o nome da função'''
    os.system('cls')
    linha = '*' * (len(texto) + 14)
    print(linha)
    print(f'|=-=-=-{texto}-=-=-=|')
    print(linha)

def opcao_invalida():
    '''Essa função serve para apresentar que a opção é inválida'''
    print('\n')
    exibir_subtitulo('Opção inválida!')
    voltar_menu()



def finalizar_app():
    '''Essa função encerra a aplicação'''
    exibir_subtitulo("Encerrando app!")

def listando_restaurantes():
    '''Esta função lista os restaurantes cadastrados'''
    exibir_subtitulo('Lista de restaurantes')
    i = int(1)
    print(f'{'Nome do restaurante'.ljust(24)}|{'Categoria'.ljust(22)}|Status')
    for item in restaurantes:
        nome_restaurante = item['nome']
        categoria = item['categoria']
        ativo = 'ativado' if item['ativo'] else 'desativado'
        
        print(f'{i}- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        i += i
    voltar_menu()

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    Inputs:
    -Nome do restaurante
    -Categoria
    
    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de restaurantes')
    print('\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    cadastro_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(cadastro_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

#main
def main():
    os.system('cls')
    exibir_nome_do_programa()
    mostrar_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()