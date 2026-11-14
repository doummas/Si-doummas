from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from numpy import *

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

app.exec_()