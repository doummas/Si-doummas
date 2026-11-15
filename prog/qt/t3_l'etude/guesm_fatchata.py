from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from pickle import *
from random import randint


def ajouter():
    f = open("msg.txt","a")
    ch=win.L1.text()
    if (ch == "" or maj(ch)==False):
        QMessageBox.critical(win,"erreur","e5tar bel s7i7")
        win.L1.clear()
        win.L1.setFocus()
    else :
        f.write(ch+"\n")
    f.close()
    
    
    
        
        
        
def afficher():
    f= open("msg.txt","r")
    ch= f.read()
    win.Li1.addItem(ch)
    
     
     
     
def coder():
    f = open("msg.txt","r")
    g= open("code.dat","wb")
    ch = f.readline()
    i=0
    while ch!="":
        ch=ch[:len(ch)-1]
        e=dict()
        e["msg1"] = codage(ch)
        ch=sans(ch)
        e["msg2"] = codage2(ch)
        dump(e,f)
        win.T.insertRow(i)
        w.T.setItem(i,0,QTableWidgetItem(e["msg1"]))
        w.T.setItem(i,1,QTableWidgetItem(e["msg2"]))
        i+=1
        ch = f.readline()
    f.close()
        
        
        
def codage(ch):
    i=0
    r=""
    while i<len(ch) :
        if ch[i] == " ":
            r=r+str(i)+"*"
        i+=1
    return r[:len(r)-1]
        
def sans(ch):
    while ch.find(" ")!=-1:
        ch=ch[:ch.find(" ")]+ch[ch.find("  ")+1:]
    return ch


def codage2(ch):
    while len(ch)%3!=0
    ch=ch + chr(randint(65,90))
    
def maj(ch):
    i=0
    while i<len(ch) and "A"<=ch[i]<="Z":
        i+=1
    return len(ch)==i
    
    
app = QApplication([])
win = loadUi("interface.ui")
win.show()
win.B1.clicked.connect (ajouter)
win.b2.clicked.connect (afficher)
win.B3.clicked.connect (coder)

app.exec_()