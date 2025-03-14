# Definimos una lista global para almacenar las notas 
notas = []

# Funcion para agregar una nota 
def agregar_nota():
    """
    Permite al usuario ingresar una nueva nota y la agrega a la lista.
    Validamos que la nota esté entre 0 y 5.
    """
    try:
        # Solicitamos la nota al usuario y permitimos decimales
        nota_individual = float(input("Ingrese la nota (0-5): "))  # Nota individual ingresada por el usuario
        if 0 <= nota_individual <= 5: # Validamos que la nota este en el rango correcto 
            notas.append(nota_individual)
            print(f"Nota {nota_individual} agregada correctamente.")
        else:
            print("La nota debe de estar entre 0 y 5.")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

# Función para mostrar todas las notas
def mostrar_notas():
     """
    Muestra todas las notas almacenadas en la lista.
    Si no hay notas, se informa al usuario.
    """
     if notas: # Verificamos que la lista de notas no este vacia 
       print("Notas registradas:")
       for i, nota in enumerate(notas, start=1):
            print(f"{i}. {nota}")
     else:
         print("No hay notas registradas.")

# Función para calcular el promedio de las notas 
def calcular_promedio():
    """
    Calcula y muestra el promedio de las notas almacenadas.
    Si no hay notas, se informa al usuario.
    """
    if notas: # Verificamos si hay notas en la lista
        promedio = sum(notas) / len(notas)
        print(f"El promedio de las notas es: {promedio:.2f}")
    else: 
        print("No hay notas registradas para calcular el promedio.")    

# Función para eliminar una nota 
def eliminar_nota():
     """
    Permite al usuario eliminar una nota específica de la lista.
    Se valida que el índice ingresado sea correcto.
    """
     if notas: # Verificamos si hay notas en la lista 
         mostrar_notas() # Mostramos las notas para que el usuario elija 
         try: 
             indice = int(input("Ingrese el número de la nota que desea eliminar: ")) - 1
             if 0 <= indice < len(notas): # Validamos que el índice esté dentro del rango 
                 nota_eliminada = notas.pop(indice)
                 print(f"Nota {nota_eliminada} eliminada correctamente.")
             else:
                 print("Índice fuera de rango.") 
         except ValueError: 
             print("Por favor, ingrese un número valido.")
     else: 
         print("No hay notas registradas para eliminar.")

# Función principal del menú
def menu():
    """
    Muestra un menú interactivo para que el usuario elija qué acción realizar.
    El programa continúa ejecutándose hasta que el usuario decida salir.
    """
    while True:
        print("\n  MENÚ DE GESTIÓN NOTAS  ") 
        print("1. Agregar nota")
        print("2. Mostrar notas")
        print("3. Calcular promedio")
        print("4. Eliminar nota")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_nota()
        elif opcion == "2":
            mostrar_notas()
        elif opcion == "3":
            calcular_promedio()
        elif opcion == "4":
            eliminar_nota()
        elif opcion == "5":
            print("¡Gracias por usar el sistema de gestión de notas!")
            break  # Salimos del bucle y terminamos el programa
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecución del programa
if __name__ == "__main__":
    menu()