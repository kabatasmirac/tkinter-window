# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:09:55 2020

@author: mirac.kabatas
"""

import os
import tkinter as tk
from tkinter import ttk

class Zoom(ttk.Frame):
    ''' Simple zoom with mouse wheel '''
    def poly(self):
        pass
    def open_image(self):
        pass
    def delete_image(self):
        pass
    def new_image(self):
        pass
    def recta(self):
        pass
    def yardim(self):
        pass
    def bilgi(self):
        pass
    # pass kısımlarına istediğiniz fonksiyonu yazabilirsiniz.

from tkinter import *   
    
class Window(Frame):
    def __init__(self, master1=None):
        Frame.__init__(self, master1)
        self.master1 = master1
        #menu oluşturup seçeneklerinin isimlendirilerek fonksiyonlara atfedilmesi
        menu = Menu(self.master1)
        self.master1.config(menu=menu)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Open Image",command=self.open_image)
        #command satırındaki her fonksiyon ismi o işi yapacak fonksiyona yönlendirir.
        fileMenu.add_command(label="Delete Current Image",command=self.delete_image)
        fileMenu.add_command(label="Open New Image",command=self.new_image)
        fileMenu.add_command(label="Exit", command=self.master.destroy)
        menu.add_cascade(label="File",menu=fileMenu)

        selectMenu = Menu(menu)
        selectMenu.add_command(label="Poligony",command=self.poly)
        selectMenu.add_command(label="Rectangle",command=self.recta)
        menu.add_cascade(label="Tool", menu=selectMenu)
 
        helpMenu = Menu(menu)
        helpMenu.add_command(label="Use",command=self.yardim)
        helpMenu.add_command(label="About",command=self.bilgi)
        menu.add_cascade(label="Help", menu=helpMenu)
        
        
#Aşağıdaki satırlarda menülerin altındaki seçeneklerin fonksiyonlarının çağırıldığı alanlar yer almaktadır.           
    def open_image(self):
        app.open_image()
    
    def delete_image(self):
        print("Siliniyor..\nDeleting..")
        app.delete_image()
        print("Silindi..\nDeleted")
        
    def new_image(self):
        app.new_image()
    def poly(self):
        print('Poligon aracı seçildi..\nPolygon tool selected..')
        app.poly()

    def recta(self):
        print('Dörtgen aracı seçildi..\nRectangle tool selected..')
        app.recta()

    def yardim(self):
        pencere = Tk()
        pencere.title("Usage of Program")
        pencere.geometry("200x400")
        uygulama = Frame(pencere)
        uygulama.grid()
        etiket = Label(uygulama,text="",font="Times 10",height=25,anchor=N,justify='left')
        etiket.grid(padx=10, pady=10)
        pencere.mainloop()
        
    def bilgi(self):
        pencere1 = Tk()
        pencere1.title("About")
        pencere1.geometry("200x300+100+200")
        uygulama1 = Frame(pencere1)
        uygulama1.grid()
        etiket1 = Label(uygulama1,text="",height=30,font="Times 10",anchor=N,justify='left')
        etiket1.grid(padx=10, pady=10)
        pencere1.mainloop()
        #yardim ve bilgi pencereleri için minik tkinter pencereleri açılarak bilgi vermektedir.
if __name__ == '__main__':
    
    root1 = Tk()
    app1 = Window(root1)
    root1.geometry("250x50")
    root1.wm_title("Tool")
    root1.mainloop()