# -*- coding: utf-8 -*-
import time
from Tkinter import *
import tkMessageBox

def hello():
    tkMessageBox.showinfo('提示', '你好，地球人')

def now():
    return time.strftime('%Y-%m-%d %H:%M:%S')

app = Tk(className='系统管理')
# app.iconbitmap('I:\\www\\favicon.ico')
# 默认窗口大小
app.geometry('300x100+960+540')
# 最小窗口大小tkMessageBox
app.minsize(300, 100)
# 最大窗口大小
app.maxsize(300, 100)

frm = Frame(app)
time = Label(frm, text=now(), cursor='tcross', font='simhei')
btn = Button(frm, text="当前时间", bitmap='', cursor='heart', command=hello, bg='red', fg='white', font='simhei')
time.pack(side=RIGHT)
btn.pack(side=LEFT)
frm.pack(side=TOP)


app.mainloop()
