#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:40:37 2018

@author: pi
"""

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.nameLabel = Label(text = 'name')
        self.nameLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text = 'hello', command = self.hello)
        self.alertButton.pack()
        
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo("Message", 'hello %s' % name)
        
        

app = Application()
app.master.title('hello')
app.mainloop()
        