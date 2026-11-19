from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from pickle import *


def ajouter():
    f = open("client.dat","ab")
    idd=win.L1.text()
    tel=win.L2.text()
    if idd == "" or tel == "":
        QMessageBox.critical(win,"erreur","Veuillez saisir les information")
    elif not(0<len(idd)<10 and alphanum(idd)):
        QMessageBox.critical(win,"erreur","Identiafiant invalid")
    elif (len(tel) !=8 or tel.isdecimal()==False):
        QMessageBox.critical(win,"erreur","Telephone invalid")
    else :
        e=dict()
        e["id"] = idd
        e["tel"]=tel
        e["genre"] = "Masculin"
        if win.R2.isChecked():
            e["genre"] = "Feminin"
        e["ville"] = win.C.currentText()
        e["etat"] = "non inscrit"
        if win.Ca.isChecked():
            e["etat"] = "inscrit"
        dump(e,f)
        QMessageBox.information(win,"info","ajoutation succes")
        f.close()
        
def alphanum(ch):
    i=0
    ch =ch.upper()
    while (i<len(ch) and ("A"<=ch[i]<="Z" or "0"<=ch[i]<="9")):
        i+=1
    return i== len(ch)


def afficher():
    f=open("client.dat","rb")
    fin = False
    i=0
    while fin == False:
        try:
            e=load(f)
            win.Ta.insertRow(i)
            win.Ta.setItem(i,0,QTableWidgetItem(e["id"]))
            win.Ta.setItem(i,1,QTableWidgetItem(e["tel"]))
            win.Ta.setItem(i,2,QTableWidgetItem(e["genre"]))
            win.Ta.setItem(i,3,QTableWidgetItem(e["ville"]))
            win.Ta.setItem(i,4,QTableWidgetItem(e["etat"]))
            i+=1
        except :
            fin=True
    f.close()
    
    
def affgagnant():
    win.Li.clear()
    f = open("client.dat","rb")
    fin = False
    while not fin:
        try:
            e=load(f)
            tel=gagn(e["tel"])
            if tel %2 == 0:
                win.Li.addItem("Les client gagant sont "+ e["id"] + "N-Telephone est " + e["tel"])
        except:
            fin = True
    f.close()
            
def gagn(n):
    while len(n)>1 :
        b=0
        for i in range(len(n)):
            b+=int(n[i])
        n=str(b)
    return int(n)
            
        
        
        
        
app = QApplication([])
win = loadUi ("proto2023.ui")
win.show()
win.B1.clicked.connect (ajouter)
win.B2.clicked.connect (afficher)
win.B3.clicked.connect(affgagnant)

app.exec_()