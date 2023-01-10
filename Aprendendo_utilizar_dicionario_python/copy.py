contatos = {
    'pauloarturob@gmail.com': {'nome': 'Paulo', 'telefone': '98638-7747'},
    # 'stefaniesdsa@gmail.com': {'nome': 'Stefanie', 'telefone': '88799-9876'},
    # 'dudalicolal@gmail.com': {'nome': 'Duda', 'telefone': '7789-0098', 'extra': {'a': 1}},
}

copia = contatos.copy()
copia['pauloarturob@gmail.com'] = {'nome': 'Gui'}

contatos['pauloarturob@gmail.com']
print(contatos) # {'pauloarturob@gmail.com': {'nome': 'Paulo', 'telefone': '98638-7747'}}

print('=' * 80)

copia ['pauloarturob@gmail.com']

print(copia) # {'pauloarturob@gmail.com': {'nome': 'Gui'}}