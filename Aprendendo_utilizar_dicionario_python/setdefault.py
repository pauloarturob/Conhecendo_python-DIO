contato = {'nome': 'Paulo', 'telefone': '98638-7747'}

print(contato)
print('=' *80)

x = contato.setdefault('nome', 'Stefanie') # Como ja existe uma chave com nome 'nome' ele nao vai sobescrever o nome
print(x) # Paulo

print(contato) # {'nome': 'Paulo', 'telefone': '98638-7747'}

y = contato.setdefault('idade', 28) # como não existe uma chave com nome idade ele ira adiciona-la no dicionário
print(y) # 28

print(contato) # {'nome': 'Paulo', 'telefone': '98638-7747', 'idade': 28}
