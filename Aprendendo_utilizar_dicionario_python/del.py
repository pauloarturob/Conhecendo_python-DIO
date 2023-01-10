contatos = {
    'pauloarturob@gmail.com': {'nome': 'Paulo', 'telefone': '98638-7747'},
    'stefaniesdsa@gmail.com': {'nome': 'Stefanie', 'telefone': '88799-9876'},
    'dudalicolal@gmail.com': {'nome': 'Duda', 'telefone': '7789-0098', 'extra': {'a': 1}},
}

del contatos['pauloarturob@gmail.com']['telefone']
del contatos['dudalicolal@gmail.com']

print(contatos) # {'pauloarturob@gmail.com': {'nome': 'Paulo'}, 'stefaniesdsa@gmail.com': {'nome': 'Stefanie', 'telefone': '88799-9876'}}