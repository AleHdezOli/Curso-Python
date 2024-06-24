#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:04:56 2024

@author: alitahdezolivares
"""
from tkinter import Tk, Label, Entry

#Diccionario
calificaciones = {'Santiago' : 8.5 , 'Lola' : 5.7 , 'Fátima' : 4.5 , 'Marina' :
                  8.3 , 'Camila' : 9.4 , 'Octavio' : 6.1 , 'Miguel' : 6.8 , 
                  'Demian' : 10 , 'Samaria' : 7.2 , 'Fernanda' : 9.1 , 'Jorge'
                  : 9.4 }
    
    
    
#Creo la ventana
ventana = Tk()
ventana.title('Calificación')
ventana.eval('tk::PlaceWindow . center')

#Creo los elementos a poner en la ventana
texto = Label(ventana, font=('Arial 15 bold'), text = '¿Cuál es tu nombre?')
entrada = Entry(ventana, font=('Arial 15 bold'), background= '#BCC07B', width=30)
score = Label(ventana, font=('Arial 15 bold'), text='')

#Pongo los elementos en la ventana
texto.pack(side = 'left', padx=(20,5), pady=10)
entrada.pack(side = 'left', padx=(2,20), pady=10)
score.pack(side= 'bottom', padx=(0,10), pady=(100,5))


#Toma el dato de la entrada depués de dar enter
#e imprime el nombre de la consola
def on_entry(event):
    nombre = entrada.get()
    resultado = calificaciones[nombre]
    score.configure(text = 'Tu calificación es: ' + str(resultado))
    print(nombre)
    

#Enlaza el recuadro de entrada con dar Return
entrada.bind('<Return>', on_entry)

ventana.mainloop()

    
