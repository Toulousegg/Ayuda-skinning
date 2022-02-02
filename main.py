from tkinter import Tk, label, Button
from tkinter.ttk import Label

class InterfazGrafica:
    def __init__(self, master):
        self.master = master
        master.title('Resizes Imagen')

        self.etiqueta = Label(master, text='Say me how much images do you gonna resize')
        self.etiqueta.pack()

        self.button_aceptar = Button(master, text='Done', command=self.button_aceptar)
        self.button_aceptar.pack()

        self.button_cerrar = Button(master, text='Exit', command=master.quit)
        self.button_cerrar.pack()

        def button_aceptar(self):
            print('Hey, wasup?')

root = Tk()
miVentana = InterfazGrafica(root)
root.mainloop()