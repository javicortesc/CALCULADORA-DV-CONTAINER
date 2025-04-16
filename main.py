import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular_digito_verificador_contenedor(contenedor):
    """
    Calcula el dígito verificador de un código de contenedor según el algoritmo especificado.

    Args:
        contenedor (str): El código del contenedor (ej. HOYU751013).

    Returns:
        int: El dígito verificador calculado (un solo dígito).
             Retorna -1 si el formato del contenedor es incorrecto.
    """
    tabla_valores = {
        'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18,
        'I': 19, 'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27,
        'Q': 28, 'R': 29, 'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36,
        'Y': 37, 'Z': 38
    }

    prefijo = contenedor[:4].upper()
    numeros = contenedor[4:]

    if len(numeros) != 6:
        return -1  # Formato incorrecto: debe tener 6 dígitos después del prefijo

    valores = []
    for i, char in enumerate(prefijo):
        if prefijo.startswith("HLCU"):
            if char == 'H':
                valores.append(4)
            elif char == 'L':
                valores.append(0)
            elif char == 'C':
                valores.append(2)
            elif char == 'U':
                valores.append(9)
            else:
                return -1  # Carácter inválido en el prefijo HLCU
        elif char in tabla_valores:
            valores.append(tabla_valores[char])
        else:
            return -1  # Carácter inválido en el prefijo

    for char in numeros:
        if char.isdigit():
            valores.append(int(char))
        else:
            return -1  # Carácter no numérico en la parte numérica

    if len(valores) != 10:
        return -1  # Error interno

    suma = 0
    for i in range(10):
        suma += valores[i] * (2 ** i)

    residuo = suma % 11
    digito_verificador = residuo

    if digito_verificador == 10:
        digito_verificador = 0

    return digito_verificador

def calcular_y_mostrar():
    """
    Función que se ejecuta al hacer clic en el botón Calcular.
    Obtiene el valor del campo de entrada, calcula el dígito verificador
    y muestra el resultado en un cuadro de mensaje.
    """
    contenedor_ingresado = entrada_contenedor.get()
    digito_calculado = calcular_digito_verificador_contenedor(contenedor_ingresado)

    if digito_calculado != -1:
        mensaje = f"El dígito verificador calculado para el contenedor {contenedor_ingresado} es: {digito_calculado}"
        messagebox.showinfo("Resultado", mensaje)  # Muestra el resultado en un messagebox
    else:
        mensaje = f"El formato del contenedor {contenedor_ingresado} es incorrecto."
        messagebox.showerror("Error", mensaje) # Muestra el error en un messagebox

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Calculadora de Dígito Verificador de Contenedor")
ventana.geometry("400x150")  # Establece el tamaño de la ventana

# Crear un frame para organizar los widgets
frame_principal = ttk.Frame(ventana, padding="20")
frame_principal.pack(fill=tk.BOTH, expand=True)

# Crear una etiqueta para el campo de entrada
etiqueta_contenedor = ttk.Label(frame_principal, text="Ingrese el código del contenedor (ej. HOYU751013):")
etiqueta_contenedor.pack(pady=5)

# Crear el campo de entrada para el código del contenedor
entrada_contenedor = ttk.Entry(frame_principal, width=30)
entrada_contenedor.pack(pady=5)

# Crear el botón para calcular el dígito verificador
boton_calcular = ttk.Button(frame_principal, text="Calcular Dígito Verificador", command=calcular_y_mostrar)
boton_calcular.pack(pady=10)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
