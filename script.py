#!/usr/bin/python

# Authors: Mojtaba Rohanian, Kamran Ghaffari 

import subprocess, os
from tkinter import *


root = Tk()
root.title("Persian Morphological Analyzer")

def analyzer(word):
    with open('./input_text.txt', 'w+') as f1:
        f1.write(word)
        f1.close()

    result = subprocess.check_output('type input_text.txt | flookup -x persianbin.foma', shell=True)
    result = result.decode('utf-8')

    f2 = open('./output_text.txt', 'w+')
    f2.write(result)
    f2.close()
    return result

def Analyze_Button():
	text_contents = text.get()
	listbox.insert(END, analyzer(text_contents))
	text.delete(0,END)

Analyze_Button = Button(root, text="Analyze! ==>", command = Analyze_Button)

text = Entry(root)

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)


text.pack(side=LEFT, fill=X, expand=1)

Analyze_Button.pack(side=LEFT)

listbox.pack(side=LEFT,fill=BOTH, expand=1)

scrollbar.pack(side=RIGHT, fill=Y)
root.geometry("600x400")


root.mainloop()
