# Importar pacotes
import tkinter as Tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from random import choice
from time import sleep
from lib_colors import *

global pontos_jog
global pontos_cpu
global icon_rock
global icon_paper
global icon_scissors
global b_icon_rock
global b_icon_paper
global b_icon_scissors

# Definir início
def inicio_jogo():

    global pontos_jog
    global pontos_cpu
    global icon_rock
    global icon_paper
    global icon_scissors
    global b_icon_rock
    global b_icon_paper
    global b_icon_scissors

    pontos_jog = 0
    pontos_cpu = 0

    icon_rock = Image.open('images/hand-rock.png')
    icon_rock = icon_rock.resize((50,50), Image.ANTIALIAS)
    icon_rock = ImageTk.PhotoImage(icon_rock)
    b_icon_rock = Button(frame_baixo,command=lambda: jogar('Pedra'),width=50,image=icon_rock,compound=CENTER,bg=cor0,fg=cor0,font=('Ivy 10 bold'),anchor=CENTER,relief=FLAT)
    b_icon_rock.place(x=15,y=60)

    icon_paper = Image.open('images/hand-paper.png')
    icon_paper = icon_paper.resize((50,50), Image.ANTIALIAS)
    icon_paper = ImageTk.PhotoImage(icon_paper)
    b_icon_paper = Button(frame_baixo,command=lambda: jogar('Papel'),width=50,image=icon_paper,compound=CENTER,bg=cor0,fg=cor0,font=('Ivy 10 bold'),anchor=CENTER,relief=FLAT)
    b_icon_paper.place(x=95,y=60)

    icon_scissors = Image.open('images/hand-scissors.png')
    icon_scissors = icon_scissors.resize((50,50), Image.ANTIALIAS)
    icon_scissors = ImageTk.PhotoImage(icon_scissors)
    b_icon_scissors = Button(frame_baixo,command=lambda: jogar('Tesoura'),width=50,image=icon_scissors,compound=CENTER,bg=cor0,fg=cor0,font=('Ivy 10 bold'),anchor=CENTER,relief=FLAT)
    b_icon_scissors.place(x=180,y=60)

# Definir função lógica
def jogar(i):

    global pontos_jog
    global pontos_cpu

    b_jogar.destroy()

    opcoes = ['Pedra','Papel','Tesoura']
    computador = choice(opcoes)
    jogador = i

    print(jogador,computador)

    if jogador == computador:
        print(f'{colors.laranja}EMPATE!{colors.fim}')
        app_linha['bg'] = cor8

    elif (jogador == 'Tesoura' and computador == 'Papel') or (jogador == 'Papel' and computador == 'Pedra') or (jogador == 'Pedra' and computador == 'Tesoura'):
        print(f'{colors.verde}O JOGADOR VENCEU!{colors.fim}')
        app_linha['bg'] = cor7
        pontos_jog += 1
        app1_pontos['text'] = pontos_jog

    else:
        print(f'{colors.vermelho}O COMPUTADOR VENCEU!{colors.fim}')
        app_linha['bg'] = cor6
        pontos_cpu += 1
        app2_pontos['text'] = pontos_cpu

# Cores
cor0 = '#FFFFFF' # branco
cor1 = '#333333' # preto
cor2 = '#fcc058' # laranja
cor3 = '#38576b' # valor
cor4 = '#3297a8' # azul
cor5 = '#fff873' # amarelo
cor6 = '#e85151' # vermelho
cor7 = '#34eb3d' # verde
cor8 = '#FF8C00' # laranja
fundo = '#3b3b3b'

# Configurar janela
janela = Tk()
janela.title('Jokenpô')
janela.geometry('260x280')
janela.configure(bg=fundo)

# Dividir janela
frame_cima = Frame(janela,width=260,height=100,bg=cor1,relief='raised')
frame_cima.grid(row=0,column=0,sticky=NW)

frame_baixo = Frame(janela,width=260,height=180,bg=cor0,relief='flat')
frame_baixo.grid(row=1,column=0,sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#Configurando o frame superior
app1 = Label(frame_cima,text="Jogador",height=1,anchor='center',font=('Ivy 10 bold'),bg=cor1,fg=cor0)
app1.place(x=25,y=70)
app1_pontos = Label(frame_cima,text="0",height=1,anchor='center',font=('Ivy 20 bold'),bg=cor1,fg=cor0)
app1_pontos.place(x=50,y=20)

app = Label(frame_cima,text=":",height=1,anchor='center',font=('Ivy 20 bold'),bg=cor1,fg=cor0)
app.place(x=125,y=20)

app2 = Label(frame_cima,text="CPU",height=1,anchor='center',font=('Ivy 10 bold'),bg=cor1,fg=cor0)
app2.place(x=200,y=70)
app2_pontos = Label(frame_cima,text="0",height=1,anchor='center',font=('Ivy 20 bold'),bg=cor1,fg=cor0)
app2_pontos.place(x=200,y=20)

app_linha = Label(frame_cima, text="",width=255,anchor='center',font=('Ivy 1 bold'), bg=cor0, fg=cor0)
app_linha.place(x=0,y=95)

# Botão Jogar
b_jogar = Button(frame_baixo,command=inicio_jogo,width=30,text="Jogar",compound=CENTER,bg=fundo,fg=cor0,font=('Ivy 10 bold'),anchor=CENTER,relief=RAISED,overrelief=RIDGE)
b_jogar.place(x=9,y=151)

janela.mainloop()