# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:34:25 2020

@author: Rony choquemaqui
"""


from tkinter import *
from math import *

ventana = Tk()
ventana.iconbitmap("UNA.ico")
ventana.title("Calculadora basica")
ventana.geometry("400x600")
ventana.resizable(False,False)
ventana.configure(background="gray15")

color_boton_operation="paleturquoise1"
color_boton_num="gray54"
color_boton_results="coral"

tamanio_cuadro=10


ancho_boton=10
alto_boton=3
operador = ""
texto_pantalla = StringVar()
def clear():
    global operador
    operador = ""
    texto_pantalla.set("0")
def click(b):
    global operador
    operador += str(b)
    texto_pantalla.set(operador)
def resultado():
    global operador
    try:
        r = str(eval(operador))
    except:
        r = "ERROR"
    texto_pantalla.set(r)
    
clear()
#primera fila
BotonRaiz = Button(ventana,text="√",bg=color_boton_operation,width=ancho_boton, 
                    height=alto_boton,command=lambda:click("sqrt")).grid(row=1,column=0,pady=tamanio_cuadro)
BotonLN = Button(ventana,text="LN",bg=color_boton_operation,width=ancho_boton,
                    height=alto_boton,command=lambda:click("log")).grid(row=1,column=1,pady=tamanio_cuadro)
BotonClear = Button(ventana,text="Borrar",bg=color_boton_results,width=ancho_boton,
                    height=alto_boton,command=clear).grid(row=1,column=2,pady=10)
BotonIgual = Button(ventana,text="=",bg=color_boton_results,width=ancho_boton,
                    height=alto_boton,command=resultado).grid(row=1,column=3,pady=tamanio_cuadro)

#segunda fila

Boton1 = Button(ventana,text="1",bg=color_boton_num,width=ancho_boton,
                height=alto_boton,command=lambda:click(1)).grid(row=2,column=0,pady=tamanio_cuadro)
Boton2 = Button(ventana,text="2",bg=color_boton_num,width=ancho_boton,
                height=alto_boton,command=lambda:click(2)).grid(row=2,column=1,pady=tamanio_cuadro)
Boton3 = Button(ventana,text="3",bg=color_boton_num,width=ancho_boton,
                height=alto_boton,command=lambda:click(3)).grid(row=2,column=2,pady=tamanio_cuadro)
BotonSuma = Button(ventana,text="+",bg=color_boton_operation,width=ancho_boton,
                   height=alto_boton,command=lambda:click("+")).grid(row=2,column=3,pady=tamanio_cuadro)
#tercera fila
Boton4 = Button(ventana,text="4",bg=color_boton_num,width=ancho_boton,
                height=alto_boton,command=lambda:click(4)).grid(row=3,column=0,pady=tamanio_cuadro)
Boton5 = Button(ventana,text="5",bg=color_boton_num,width=ancho_boton,
                height=alto_boton,command=lambda:click(5)).grid(row=3,column=1,pady=tamanio_cuadro)
Boton6 = Button(ventana,text="6",bg=color_boton_num,width=ancho_boton,
                height=alto_boton,command=lambda:click(6)).grid(row=3,column=2,pady=tamanio_cuadro)
BotonResta = Button(ventana,text="-",bg=color_boton_operation,width=ancho_boton,
                    height=alto_boton,command=lambda:click("-")).grid(row=3,column=3,pady=tamanio_cuadro)
#cuarta fila
Boton7 = Button(ventana,text="7",bg=color_boton_num,width=ancho_boton,
                height=alto_boton,command=lambda:click(7)).grid(row=4,column=0,pady=tamanio_cuadro)
Boton8 = Button(ventana,text="8",bg=color_boton_num,width=ancho_boton,
                height=alto_boton,command=lambda:click(8)).grid(row=4,column=1,pady=tamanio_cuadro)
Boton9 = Button(ventana,text="9",bg=color_boton_num,width=ancho_boton,
                height=alto_boton,command=lambda:click(9)).grid(row=4,column=2,pady=tamanio_cuadro)
BotonMult = Button(ventana,text="x",bg=color_boton_operation,width=ancho_boton,
                   height=alto_boton,command=lambda:click("*")).grid(row=4,column=3,pady=tamanio_cuadro)
#quita fila
BotonParenIzq = Button(ventana,text="(",bg=color_boton_num,width=ancho_boton,
                height=alto_boton,command=lambda:click("(")).grid(row=5,column=0,pady=tamanio_cuadro)
Boton0 = Button(ventana,text="0",fg="blue", bg=color_boton_num,width=ancho_boton,
                height=alto_boton,command=lambda:click(0)).grid(row=5,column=1,pady=tamanio_cuadro)
BotonParenDer = Button(ventana,text=")",bg=color_boton_num,width=ancho_boton,
                      height=alto_boton,command=lambda:click(")")).grid(row=5,column=2,pady=tamanio_cuadro)
BotonDiv = Button(ventana,text="/",bg=color_boton_operation,width=ancho_boton,
                  height=alto_boton,command=lambda:click("/")).grid(row=5,column=3,pady=tamanio_cuadro)
#sexta fila
BotonPi = Button(ventana,text="π",bg=color_boton_num,width=ancho_boton,
                 height=alto_boton,command=lambda:click("pi")).grid(row=6,column=0,pady=tamanio_cuadro)
BotonPunto = Button(ventana,text=".",bg=color_boton_num,width=ancho_boton,
                    height=alto_boton,command=lambda:click(".")).grid(row=6,column=1,pady=tamanio_cuadro)
BotonEXP = Button(ventana,text="EXP",bg=color_boton_operation,width=ancho_boton,
                  height=alto_boton,command=lambda:click("exp")).grid(row=6,column=2,pady=tamanio_cuadro)
BotonMod = Button(ventana,text="%",bg=color_boton_operation,width=ancho_boton,
                  height=alto_boton,command=lambda:click("%")).grid(row=6,column=3,pady=tamanio_cuadro)

Pantalla = Entry(ventana,font=("arial",20,"bold"),width=22,
                 borderwidth=10,background="lightcyan2",textvariable=texto_pantalla)
Pantalla.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

ventana.mainloop()
