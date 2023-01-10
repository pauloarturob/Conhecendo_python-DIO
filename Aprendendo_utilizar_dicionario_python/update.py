contatos = {
    'pauloarturob@gmail.com': {'nome': 'Paulo', 'telefone': '98638-7747'},
}
contatos.update({'pauloarturob@gmail.com': {'nome': 'Stefanie'}})

print(contatos) # {'pauloarturob@gmail.com': {'nome': 'Stefanie'}}

contatos.update({'stefaniesdsa@gmail.com': {'nome': 'Maria Alice', 'telefone': '77889-0098'}})
print(contatos) # {'pauloarturob@gmail.com': {'nome': 'Stefanie'}, 'stefaniesdsa@gmail.com': {'nome': 'Maria Alice', 'telefone': '77889-0098'}}