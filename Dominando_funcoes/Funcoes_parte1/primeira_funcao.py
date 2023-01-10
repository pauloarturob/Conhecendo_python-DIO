def exibir_mensagem():
    print('Ola mundo')

def exibir_mensagem2(nome):
    print(f'Seja bem vindo {nome}')

def exibir_mensagem3(nome = 'Anonimo'):
    print(f'Seja bem vindo {nome}!')


exibir_mensagem() # Ola mundo
exibir_mensagem2(nome='Paulo') # Seja bem vindo Paulo
exibir_mensagem3() # Seja bem vindo Anonimo!
exibir_mensagem3(nome='Stefanie') # Seja bem vindo Stefanie!
