#coding: utf-8

import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import Tk, Canvas, mainloop, RIGHT, filedialog
from tkinter import Button, DISABLED, CENTER, colorchooser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BTN_CONFIG = {
    "border": "0",
    "activebackground": "#BED8D4",
    "background": "#EFF6EE",
    "bd": "0",
    "borderwidth": 0,
    "foreground": "#5B5B63",
    "activeforeground": "#5B5B63",
    "font": "Bold",
}

class Window():
    def __init__(self, width=300, height=400, background="#FCFCFC"):
        try:
            self.imagemOriginal = None
            self.imagemAlterada = None
            self.root = Tk()
            self.root.title('CGPI')
            self.canvas = Canvas(self.root, width=width, height=height, bg=background)
            self.canvas.pack(side=RIGHT)
                
            #Botões
            self.btn1 = Button(self.root, BTN_CONFIG, text="Selecionar arquivo", command=self.abrirArquivo)
            self.btn1.place(height=40, width=200, x= 50, y=30)

            self.btn2 = Button(self.root, BTN_CONFIG, text="Binarizar imagem", command=self.binarizarImagem)
            self.btn2.place(height=40, width=200, x=50, y=80)

            self.btn3 = Button(self.root, BTN_CONFIG, text="Histograma", command=self.histograma)
            self.btn3.place(height=40, width=200, x=50, y=130)

            self.btn4 = Button(self.root, BTN_CONFIG, text="Escala de cinza", command=self.padraoDeCinza)
            self.btn4.place(height=40, width=200, x=50, y=180)

            self.btn5 = Button(self.root, BTN_CONFIG, text="Filtro blur", command=self.filtroBlur)
            self.btn5.place(height=40, width=200, x=50, y=230)

            self.btn6 = Button(self.root, BTN_CONFIG, text="Filtro negativo", command=self.filtroNegativo)
            self.btn6.place(height=40, width=200, x=50, y=280)

            self.btn7 = Button(self.root, BTN_CONFIG, text="Salvar imagem", command=self.salvar)
            self.btn7.place(height=40, width=200, x=50, y=330)

        except Exception as e:
            print("window init: ", type(e), e)
            raise e

    def open(self):
        try:
            mainloop()
        except Exception as e:
            print("window open: ", type(e), e)
            raise e
        
    def abrirArquivo(self):
        try:
            filename = filedialog.askopenfilename(
                        initialdir=BASE_DIR, title="Selecione o aquivo JPG.",
                        filetypes=(("Arquivos JPG", "*.jpg"), ("todos os arquivos", "*.*"))
                    )
            if filename:
                self.imagemOriginal = cv2.imread(filename, 1)
                self.imagemAlterada = self.imagemOriginal
                cv2.imshow("Imagem original", self.imagemOriginal)
                
        except Exception as e:
                print("Erro em abir arquivo: ", type(e), e)
                raise e
        
    def binarizarImagem(self):
        #retorna dois parametros, o limiar que defini e a imagem apos a binarização
        #150 é o lmiar que eu defini, 255(preto) será a cor que os pixel irão receber se forem maiores que o limiar
        self.imagemAlterada = cv2.cvtColor(self.imagemOriginal, cv2.COLOR_BGR2GRAY)
        limiar, self.imagemAlterada = cv2.threshold(self.imagemAlterada, 150, 255, cv2.THRESH_BINARY)

        cv2.imshow("Imagem binarizada", self.imagemAlterada)

    def histograma(self):
        plt.hist(self.imagemAlterada.ravel(), 256, [0, 256])
        plt.show()
            
    def padraoDeCinza(self):
        self.imagemAlterada = cv2.cvtColor(self.imagemOriginal, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Imagem em escala de cinza", self.imagemAlterada)

    def filtroBlur(self):
        self.imagemAlterada = cv2.GaussianBlur(self.imagemOriginal, (17, 17), 0) 
        cv2.imshow('Imagem com filtro blur', self.imagemAlterada ) 

    def filtroNegativo(self):
        self.imagemAlterada = (255-self.imagemOriginal)
        cv2.imshow('Imagem com filtro negativo', self.imagemAlterada)
    
    def salvar(self):
        try:
            nome = filedialog.asksaveasfilename()
            if nome:
                cv2.imwrite(nome, self.imagemAlterada)

        except Exception as e:
            print("salvar2: ", type(e), e)
            raise e    
def main():
    try:
        window = Window()
        window.open()

    except Exception as e:
        print("main: ", type(e), e)
        raise e

main()



