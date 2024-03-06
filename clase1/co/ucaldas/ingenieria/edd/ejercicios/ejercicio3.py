def suma_elementos(lista):
   suma = 0
   for elemento in lista:
       suma += elemento
   return suma

lista_usuario = input("Ingresa una lista de números separados por comas: ")
numeros = [int(numero) for numero in lista_usuario.split(',')]
resultado = suma_elementos(numeros)
print("La suma de los elementos de la lista es:", resultado)