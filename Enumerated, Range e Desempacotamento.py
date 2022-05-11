idades = [15, 25, 36, 44, 46, 88]

# for i in enumerate(idades): #Usando a bultin enumerate para posição + item da lista;
#     print(i)

# for indice, idade in enumerate(idades): #Desempacotando tupla;
#     print(indice, idade)

# for i in range(len(idades)): #Forma simples de posição + item da lista;
#     print(i, idades[i])

usuario = [("Igor", 35, 1984), ("Cecilia", 7, 2013), ("Cladia", 36, 1983)]

for nome, idade, ano in usuario: #Desempacotando tuplas e usando somente o nescesario;
    print(nome)