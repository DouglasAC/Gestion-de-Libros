from tkinter import *

# Crear la ventana principal
window = Tk()

# Etiquetas para los campos de entrada
l1 = Label(window, text="Titulo")
l1.grid(row=0, column=0)

l2 = Label(window, text="Autor")
l2.grid(row=0, column=2)

l3 = Label(window, text="Año")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Campos de entrada para los datos
titulo_valor = StringVar()
e1 = Entry(window, textvariable=titulo_valor)
e1.grid(row=0, column=1)

autor_valor = StringVar()
e2 = Entry(window, textvariable=autor_valor)
e2.grid(row=0, column=3)

anio_valor = StringVar()
e3 = Entry(window, textvariable=anio_valor)
e3.grid(row=1, column=1)

isbn_valor = StringVar()
e4 = Entry(window, textvariable=isbn_valor)
e4.grid(row=1, column=3)

# Lista para mostrar los datos y barra de desplazamiento
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# Vincular la lista y la barra de desplazamiento
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Botones para las acciones
b1 = Button(window, text="Ver todos", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Buscar entrada", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Agregar entrada", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Actualizar seleccion", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Borrar seleccion", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Cerrar", width=12)
b6.grid(row=7, column=3)

# Mostrar la ventana
window.mainloop()