""" ADV GUESSING NUMB """

#

import tkinter as tk
from tkinter import messagebox
import random 

#variabili globali

num_segr = random.randint(1,100)
tentativi = 0

#funzioni controllo
def controlla():
    global tentativi

    try:
        guess = int(entry.get())
        tentativi += 1
        label_tentativi.config(text=f'Tentativi: {tentativi}')

        if guess < num_segr:
            label_feedback.config(text= 'Troppo basso!')
        elif guess > num_segr:
            label_feedback.config(text= 'Troppo alto!')
        

#reset partita
def nuova_partita():
    global num_segr, tentativi
    num_segr = random.randint(1,100)
    tentativi = 0
    label_feedback



#GUI
root = tk.Tk()
root.title('Guessing game base')
root.geometry('300x200')

label_title = tk.label(root, text= 'Indovina il numero (1, 100)')
label_title.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text='Indovina', command=controlla)
btn.pack(pady=5)

label_feedback = tk.Label(root, text="")
label_feedback.pack()

btn_reset = tk.Button(root, text= '')