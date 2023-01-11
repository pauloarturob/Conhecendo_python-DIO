def cria_carro(*, modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

cria_carro('Palio', 1999, 'ABC-1983', marca='Fiat', motor='1.0', combustivel='Gasolina') # Essa condição e invalida

cria_carro(modelo='Palio', ano=1999, placa='ABC-1983', marca='Fiat', motor='1.0', combustivel='Gasolina') # Essa condição e valida