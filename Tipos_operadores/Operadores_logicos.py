# and =  para ser True tudo tem que ser True
# or =  para ser True apenas um tem que ser True

print(True and True and True)
print(False and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

saldo = 1000
saque = 200
limite = 100

#--------------------------and------------------------------------------

saldo >= saque and saque <= limite #false , se para ser verdadeira todos tem que ser verdadeiros

#--------------------------or--------------------------------------------

saldo >= saque or saque <= limite #verdadeiro, para que seja false todos tem que ser falso


#--------------------------operadores de negação--------------------------
contatos_emergencia = []

not 1000 > 1500  # ser torna verdadeiro pq a um 'not' de negação no inicio
# true

not contatos_emergencia  # lista vazia em python e falso como esta em negação se torna verdadeiro
# true

not "saque 1500"  # a string é verdadeira ela tem valor como a uma negação se torna false
# false

not ""  # string vazia nao tem valor e false porem esta com negação e torna verdadeira
# true


#--------------------------Paraneteses------------------------------------------

saldo = 1000
saque = 250
limite = 200
conta_especial = True

resul = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(resul)

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)


#outro modo de montar a expressão

conta_normal =  saldo >= saque and saque <= limite
conta_especial_suficiente = conta_especial and saldo >= saque

resolucao = conta_normal or conta_especial_suficiente
print(resolucao)


