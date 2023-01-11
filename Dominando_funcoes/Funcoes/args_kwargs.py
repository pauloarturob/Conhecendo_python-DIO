def exibir_poema(data_extensao, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extensao}\n\n {texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema('Terça, 10 janeiro de 2023', 'Zen of python', 'Beautiful is better than ugly.', autor='Tim Peters', ano=1999)