from arbol import Arbol

arbol = Arbol("Luis")
arbol.insertar(arbol.raiz, "Maria Fernanda")
arbol.insertar(arbol.raiz,"Sofia")
arbol.insertar(arbol.raiz,"Alexander")
arbol.insertar(arbol.raiz,"Jack")
arbol.insertar(arbol.raiz,"Jace")

nombre = input("Agrega datos al arbol:")
arbol.insertar(arbol.raiz, nombre)

busqueda = input("Busca datos en el arbol:")
nodo = arbol.buscar(arbol.raiz, busqueda)
if nodo is None:
    print(f"{busqueda} No existe")
else:
    print(f"{busqueda} Si existe")