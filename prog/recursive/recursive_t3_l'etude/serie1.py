def lettre(ch):
    if len(ch)<1:
        return ""
    elif ch[0].isdecimal()==False:
        return ch[0]+lettre(ch[1:])
    else:
        return lettre(ch[1:])
    
    



def chiffre (n,k):
    if k==1:
        return n%10
    else:
        return chiffre((n-(n%10))//10,k-1)
    
    

def Traitement(n,r):
    if n==0:
        return r
    else:
        return Traitement(n//10,r*(n%10))
    

    
    
from random import randint
from numpy import *
n=10
T=array([int]*n)
def remplir(T,n):
    for i in range(n):
        T[i]=randint(1,99)
    for i in range(n):
        print(T[i],end="|")
    
def grand(T,n):
    if n == 0:
        return T[0]
    elif   T[n]>T[0]  :
        aux = T[n]
        T[n] = T[0]
        T[0] = aux
        return grand(T,n-1)
    else :
        return grand(T,n-1)
remplir(T,n)    
print("\n",grand(T,n-1))

r=10
M=array([[int()]*r]*r)

def remplirM(M,r):
    for i in range(r):
        for j in range(r):
            M[i,j] = randint(1,11)
    for i in range(r):
        for j in range(r):
            print(M[i,j],end="|")
        print()
def somme(M,i,j):
    if i==0 and j==0:
        return M[i,j]
    elif i>0 and j>= i  :
        if i==0:
            i=j
        return somme(M[i,j]+M[i-1,j],i-1,j)
    else:
        if j==0:
            j=i
        return somme(M[i,j-1]+M[i,j],i,j-1)# 8alta toul ou 3ordh ou nhb nmchi ya nor9d bkri lila ya nl3b 
        
remplirM(M,r)
print(somme(M,r,r))


