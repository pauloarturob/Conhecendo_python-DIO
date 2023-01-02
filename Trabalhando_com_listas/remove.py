linguagens = ['python', 'js', 'c', 'java', 'csharp']

linguagens.remove('c')

print(linguagens) #['python', 'js', 'java', 'csharp']

#Essa funcção remove o objeto que esta dentra de uma lista, mas se tiver mais de um objeto igual na mesma lista ele somente tira um
#objeto ex:

linguagens = ['python', 'js', 'c', 'java', 'csharp', 'c']

linguagens.remove('c')

print(linguagens) # ['python', 'js', 'java', 'csharp', 'c']