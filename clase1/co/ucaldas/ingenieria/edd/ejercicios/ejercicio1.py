lista = []

while True:
   elemento = input("Ingrese un elemento o escriba 'fin' para salir: ")
   if elemento == 'fin':
       break
   lista.append(elemento)

print("Su lista es:", lista)