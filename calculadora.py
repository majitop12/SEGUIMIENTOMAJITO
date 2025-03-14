# El bucle while permite que el programa ejecute continuamente.
# Finaliza cuando el usuario lo indique 
while   True:
    # Mostrar un menú de la calculadora.
    print("\n========MENÚ CALCULADORA========")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")

    # Se solicita al usuario que elija una opción del menú
    opcion = input("Elija una opción (1-3): ")

    # Opción 1: Suma

    if opcion == "1":
        num1 =float(input("Ingrese el primer número: "))
        num2 =float(input("Ingrese el sengundo número: "))

        # calcular la suma
        resultado = num1+num2
        # Mostrar resultado
        print(f"El resultado es: {resultado}")

    # Opción 2: Resta
    elif opcion == "2":
        num1 =float(input("Ingrese el primer número: "))
        num2 =float(input("Ingrese el sengundo número: "))

        # calcular la resta
        resultado = num1+num2
        # Mostrar resultado
        print(f"El resultado es: {resultado}")
    
    # Opción 3: Salir del programa
    elif opcion == "3":
        # Mensaje de cierre
        break # Termina el bucle while
    
    # Opcion inválida
    else: 
        print("Opción invalida. Por favor, seleccione una opcion del 1 al 3.")
    
    input("Presione enter para continuar...")
    
# Importar las Librerias necesarias
from tkinter import Tk, Label, Button, Entry


def crear_ventana():
    # Configurar colores y fuentes
    bg_color = "#F0F0F0"  # FONDO CLARO
    fg_color = "#333"
    font = ("Arial", 12)

    # Crear la Ventana Principal
    vent = Tk()
    vent.title("Calculadora Simple")
    vent.geometry("500x300")
    vent.configure(bg=bg_color)  # El color del fondo de la ventana

    # Agragar un Label
    label_hi = Label(
        vent, text="Calculadora basica para Suma y Resta", font=("Arial", 14), fg="#933571")
    label_hi.pack(pady=20)

    # Definir la Función SUMA
    def fnSuma():
        n1 = txt1.get()
        n2 = txt2.get()
        r = float(n1) + float(n2)
        txt3.delete(0, 'end')
        txt3.insert(0, r)

    def fnSalir():
        vent.destroy()

    # Crear en elntorno de la Interfaz
    # Crer la Etiqueta y el campo de texto del primer numero
    lbl1 = Label(vent, text="Primer Numero",
                 font=font, fg=fg_color, bg=bg_color)
    lbl1.place(relx=0.5, rely=0.3, anchor="center",
               relheight=0.1, relwidth=0.6)
    txt1 = Entry(vent, bg="#FFF")
    txt1.place(relx=0.5, rely=0.4, anchor="center",
               relheight=0.1, relwidth=0.6)

    vent.mainloop()


# Crea la Ventana Pincipal
vent = crear_ventana()

# Iniciar la Aplicación
# vent.mainloop()cls
 


    