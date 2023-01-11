salario = 2000

def salario_bonus(bonus):
    global salario
    salario +=bonus    # Nesse modelo a variavel salario esta declara global
    return salario
print(salario_bonus(500)) # 2500

def salario_bonus(bonus):
    salario = 2000
                                # Nesse modelo a variavel salario foi declarada local ae nao gera erro
    salario +=bonus
    return salario
print(salario_bonus(500))
