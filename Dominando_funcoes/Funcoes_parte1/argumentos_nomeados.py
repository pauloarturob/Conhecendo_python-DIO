def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')


salvar_carro('Fiat', 'Palio', '1999', 'ABC-1983') # Carro inserido com sucesso! Fiat/Palio/1999/ABC-1983
salvar_carro(marca='Fiat', modelo='Palio', ano=1999, placa='ABC-1983') # Carro inserido com sucesso! Fiat/Palio/1999/ABC-1983
salvar_carro(**{'marca': 'Fiat', 'modelo': 'palio', 'ano': 1999, 'placa': 'ABC-1983'}) # Carro inserido com sucesso! Fiat/Palio/1999/ABC-1983
