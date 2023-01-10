contatos = {
    'pauloarturob@gmail.com': {'nome': 'Paulo', 'telefone': '98638-7747'},
    'stefaniesdsa@gmail.com': {'nome': 'Stefanie', 'telefone': '88799-9876'},
    'dudalicolal@gmail.com': {'nome': 'Duda', 'telefone': '7789-0098', 'extra': {'a': 1}},
}
for chave, valor in contatos.items(): # usei dessa forma so para ficar com a impressão mais bonita
    print(chave, valor)


print('=' * 80)

contatos.clear()
print(contatos) # {}