#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Working
from tkinter import *
main = Tk()
main.title('NETWORK')
def convert():
    Ans=''
    blank.delete(0, END)
    strn = num1.get()
    for i in range(0,len(strn)):
        if(strn[i] == ' '):
            Ans+=' '
            continue
        if(ord(strn[i])<91):
            Ans+=chr(26 - (ord(strn[i])-65)+64)
        else:
            Ans+=chr(26 - (ord(strn[i])-97)+96)
    blank.insert(0, Ans)
    
main.geometry('500x100')
Label(main, text = "Enter Num 1:").grid(row=0, column = 0)
Label(main, text = "The Answer is:").grid(row=2, column=0)


num1 = Entry(main)
num1.focus_set()
blank = Entry(main)


num1.grid(row=0, column=1)
blank.grid(row=2, column=1)


Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W)
Button(main, text='Encipher', command=convert).grid(row=0, column=3, sticky=W)
Button(main, text='Decipher', command=convert).grid(row=0, column=4, sticky=W)

mainloop()

