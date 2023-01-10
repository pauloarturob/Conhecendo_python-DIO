contatos = {
    'pauloarturob@gmail.com': {'nome': 'Paulo', 'telefone': '98638-7747'},
    'stefaniesdsa@gmail.com': {'nome': 'Stefanie', 'telefone': '88799-9876'},
    'dudalicolal@gmail.com': {'nome': 'Duda', 'telefone': '7789-0098', 'extra': {'a': 1}},
}

x = 'pauloarturob@gmail.com' in contatos
print(x) # True

y = 'maria@gmail.com' in contatos
print(y) # False

z = 'idade' in contatos['pauloarturob@gmail.com']
print(z) # False

j = 'telefone' in contatos['stefaniesdsa@gmail.com']
print(j) # True
