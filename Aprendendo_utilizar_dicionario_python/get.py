contatos = {
    'pauloarturob@gmail.com': {'nome': 'Paulo', 'telefone': '98638-7747'},
}
# contatos['chave']

# print(contatos) # KeyError: 'chave'

x = contatos.get('chave')
print(x) # None
print('=' * 80)
y = contatos.get('chaves', {})
print(y) # {}
print('=' * 80)
z = contatos.get('pauloarturob@gmail.com', {})
print(z) # {'nome': 'Paulo', 'telefone': '98638-7747'}

