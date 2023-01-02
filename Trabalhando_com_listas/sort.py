linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort()
print(linguagens) #['c', 'csharp', 'java', 'js', 'python'] Somente Sort ele ira ordernar a lista em ordem alfabetica

linguagens.sort(reverse=True)
print(linguagens) # ['python', 'js', 'java', 'csharp', 'c']

linguagens.sort(key=lambda x: len(x))
print(linguagens) #['c', 'js', 'java', 'python', 'csharp']

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens) #['python', 'csharp', 'java', 'js', 'c']