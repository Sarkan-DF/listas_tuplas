idade = [15, 55, 11, 98, 23, 54, 5]

#Usando o sorted + reverse;
# print(sorted(idade, reverse=True))
# print(idade)
# print(list(reversed(idade)))

#O sorted só muda localmente;
idade_ordenadas = sorted(idade)
print(idade_ordenadas)
print(idade)

#O list.sort muda a lista mesmo tomar cuidado;
# list.sort(idade) #O list.sort muda a lista mesmo tomar cuidado.
# print(idade)