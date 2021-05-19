from tkinter import *
import sistema
from threading import Thread
import asyncio

import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import animation

class monitor:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "15")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.pack()

        self.container15 = Frame(master)
        self.container15["padx"] = 20
        self.container15["pady"] = 5    
        self.container15.pack()
        self.container16 = Frame(master)
        self.container16["padx"] = 20
        self.container16["pady"] = 10
        self.container16.pack()
        self.container17 = Frame(master)
        self.container17["pady"] = 15
        self.container17.pack()

        self.titulo = Label(self.container1, text="Monitor de Recursos")
        self.titulo["font"] = ("Calibri", "15", "bold")
        self.titulo.pack ()

        self.espaco = Label(self.container2, text="",
        font=self.fonte, width=25)
        self.espaco.pack(side=LEFT)

        self.btnAtualizar = Button(self.container2, text="Atualizar",
        font=self.fonte, width=10)
        self.btnAtualizar["command"] = self.atualizar
        self.btnAtualizar.pack(side=RIGHT)

        self.lbCpuTemp = Label(self.container3, text="CPU-Temp:",
        font=self.fonte, width=11)
        self.lbCpuTemp.pack(side=LEFT)

        self.entCpuTemp = Entry(self.container3)
        self.entCpuTemp["width"] = 25
        self.entCpuTemp["font"] = self.fonte
        self.entCpuTemp.pack(side=LEFT)

        self.lbCpuFreq = Label(self.container4, text="CPU-Freq:",
        font=self.fonte, width=11)
        self.lbCpuFreq.pack(side=LEFT)

        self.entCpuFreq = Entry(self.container4)
        self.entCpuFreq["width"] = 25
        self.entCpuFreq["font"] = self.fonte
        self.entCpuFreq.pack(side=LEFT)

        self.lbCpuMedia= Label(self.container5, text="CPU-Media:",
        font=self.fonte, width=11)
        self.lbCpuMedia.pack(side=LEFT)

        self.entCpuMedia = Entry(self.container5)
        self.entCpuMedia["width"] = 25
        self.entCpuMedia["font"] = self.fonte
        self.entCpuMedia.pack(side=LEFT)

        self.lbCpuUso= Label(self.container6, text="CPU-Uso:",
        font=self.fonte, width=11)
        self.lbCpuUso.pack(side=LEFT)

        self.entCpuUso = Entry(self.container6)
        self.entCpuUso["width"] = 25
        self.entCpuUso["font"] = self.fonte
        self.entCpuUso.pack(side=LEFT)


        self.lbMemoUso= Label(self.container7, text="Memo-Uso:",
        font=self.fonte, width=11)
        self.lbMemoUso.pack(side=LEFT)

        self.entMemoUso = Entry(self.container7)
        self.entMemoUso["width"] = 25
        self.entMemoUso["font"] = self.fonte
        self.entMemoUso.pack(side=LEFT)

        self.lbMemoDisp= Label(self.container8, text="Memo-Disp:",
        font=self.fonte, width=11)
        self.lbMemoDisp.pack(side=LEFT)

        self.entMemoDisp = Entry(self.container8)
        self.entMemoDisp["width"] = 25
        self.entMemoDisp["font"] = self.fonte
        self.entMemoDisp.pack(side=LEFT)

        self.lbMemoPorc= Label(self.container9, text="Memo-Porc:",
        font=self.fonte, width=11)
        self.lbMemoPorc.pack(side=LEFT)

        self.entMemoPorc = Entry(self.container9)
        self.entMemoPorc["width"] = 25
        self.entMemoPorc["font"] = self.fonte
        self.entMemoPorc.pack(side=LEFT)

        self.lbMemoLivre= Label(self.container10, text="Memo-Livre:",
        font=self.fonte, width=11)
        self.lbMemoLivre.pack(side=LEFT)

        self.entMemoLivre = Entry(self.container10)
        self.entMemoLivre["width"] = 25
        self.entMemoLivre["font"] = self.fonte
        self.entMemoLivre.pack(side=LEFT)

        self.lbFanVel= Label(self.container11, text="Fan-Vel:",
        font=self.fonte, width=11)
        self.lbFanVel.pack(side=LEFT)

        self.entFanVel = Entry(self.container11)
        self.entFanVel["width"] = 25
        self.entFanVel["font"] = self.fonte
        self.entFanVel.pack(side=LEFT)

        self.bntInsert = Button(self.container16, text="",
        font=self.fonte, width=12)
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container16, text="",
        font=self.fonte, width=12)
        self.bntAlterar.pack (side=LEFT)

        self.bntGraficos = Button(self.container16, text="Graficos",
        font=self.fonte, width=12)
        self.bntGraficos.pack(side=LEFT)
        self.bntGraficos["command"]= self.criarNovaTela

        self.lblmsg = Label(self.container17, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def atualizar(self):
        while TRUE:
            async def iniciarAtt(self):
                valores = sistema.coletasDadosAtual()

                self.entCpuUso.delete(0, END)
                self.entCpuUso.insert(INSERT, valores[0])

                self.entCpuTemp.delete(0, END)
                self.entCpuTemp.insert(INSERT, valores[3])

                self.entCpuFreq.delete(0, END)
                self.entCpuFreq.insert(INSERT,valores[1])

                self.entCpuMedia.delete(0, END)
                self.entCpuMedia.insert(INSERT, valores[2])

                self.entMemoUso.delete(0, END)
                self.entMemoUso.insert(INSERT, valores[4])

                self.entMemoDisp.delete(0, END)
                self.entMemoDisp.insert(INSERT, valores[5])

                self.entMemoPorc.delete(0, END)
                self.entMemoPorc.insert(INSERT, valores[6])

                self.entMemoLivre.delete(0, END)
                self.entMemoLivre.insert(INSERT, valores[7])

                self.entFanVel.delete(0, END)
                self.entFanVel.insert(INSERT, valores[8])

            asyncio.run(iniciarAtt(self))


    def criarNovaTela(self):
        fig, ax = plt.subplots()

        def animar():
            x=[0,1,3]
            y=[20,30,50]
            ax.clear()
            ax.plot([1,2,3,4],[1,4,9,16])
            ax.set_xlabel('teste')
        

        animar()

        """ newWindow = Toplevel()
        labelExample = Label(newWindow, text = "Graficossss aquiii")
        botgraficos = Button(newWindow, text="teste grafico", command=graficoPlot)

        labelExample.pack()
        botgraficos.pack() """
 
        
        


root = Tk()
monitor(root)
root.mainloop()