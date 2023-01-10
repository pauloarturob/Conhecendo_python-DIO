contatos = {
    'pauloarturob@gmail.com': {'nome': 'Paulo', 'telefone': '98638-7747'},
    'stefaniesdsa@gmail.com': {'nome': 'Stefanie', 'telefone': '88799-9876'},
    'dudalicolal@gmail,.com': {'nome': 'Duda', 'telefone': '7789-0098', 'extra': {'a': 1}},

}
# acessando dados do dicionário

extra = contatos['dudalicolal@gmail,.com']['extra']

print(extra) # {'a': 1}

telefone = contatos['pauloarturob@gmail.com']['telefone']

print(telefone) # 98638-7747

