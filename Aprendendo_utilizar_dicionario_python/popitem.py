contatos = {
    'pauloarturob@gmail.com': {'nome': 'Paulo', 'telefone': '98638-7747'},
}

x = contatos.popitem() # como nao informamos a chave ele retira todos itens em sequencia
print(x) # ('pauloarturob@gmail.com', {'nome': 'Paulo', 'telefone': '98638-7747'})

y = contatos.popitem()
print(y)