tuplas = ['P', 'y', 't', 'h', 'o', 'n']

tuplas[2:] # ['t', 'h', 'o', 'n'] pega do segundo item para frente
tuplas[:2] # ['P', 'y'] pega do 1 item até o 1
tuplas[1:3] # ['y', 't']
tuplas[0:3:2] # ['P', 't']
tuplas[::] # ['P', 'y', 't', 'h', 'o', 'n'] pega a tuplas toda
tuplas[::-1] # ['n', 'o', 'h', 't', 'y', 'P']

print(tuplas[2:])
print(tuplas[:2])
print(tuplas[1:3])
print(tuplas[0:3:2])
print(tuplas[::])
print(tuplas[::-1])