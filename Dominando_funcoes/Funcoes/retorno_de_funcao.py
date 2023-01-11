def calcula_total(numeros):
    return sum(numeros)


def retornar_antecessor_e_sucessor(numero):
    antecessoor = numero - 1
    sucessor = numero + 1

    return antecessoor, sucessor

def func_3():
    print('Ola de novo')

print(calcula_total([10, 20, 34])) # 64
print(retornar_antecessor_e_sucessor(10)) # (9, 11)
func_3()
