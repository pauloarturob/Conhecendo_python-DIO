contatos = {
    'pauloarturob@gmail.com': {'nome': 'Paulo', 'telefone': '98638-7747'},
    'stefaniesdsa@gmail.com': {'nome': 'Stefanie', 'telefone': '88799-9876'},
    'dudalicolal@gmail.com': {'nome': 'Duda', 'telefone': '7789-0098', 'extra': {'a': 1}},

}

for chave in contatos: # 1 forma de obter valores da chave dos contatos porem não e a mais usada ou indicada
    print(chave, contatos[chave])
print('=' * 100)
for chave, valor in contatos.items(): # 2 forma de obter valores da chave dos contatos e mais indicada para uso
    print(chave, valor)