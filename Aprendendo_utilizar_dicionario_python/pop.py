contatos = {
    'pauloarturob@gmail.com': {'nome': 'Paulo', 'telefone': '98638-7747'},
}

x = contatos.pop('pauloarturob@gmail.com')
print(x) # {'nome': 'Paulo', 'telefone': '98638-7747'}

print('=' * 80)

y = contatos.pop('pauloarturob@gmail.com', {})
print(y) # {}