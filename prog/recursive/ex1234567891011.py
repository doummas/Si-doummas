from numpy import *


def pgcd(a,b):
        if b==0:
            return a
        else :
            return pgcd(b,a%b)
        
        





def chaine(ch):
    if len(ch)<1:
        return ""
    else:
        return ch[len(ch)-1] + chaine(ch[:len(ch)-1])
    





def chercher(ch,c):
    if ch[0] == c:
        return True
    elif len(ch)==1:
        return c==ch[0]
    else:
        return chercher(ch[1:],c)
    



def chercher_ent(ch,c):
    if ch == 0:
        return False
    elif ch//(puis(str(ch)))==c:
        return True
    else :
        return chercher_ent(ch%(puis(str(ch))),c)
        
def puis(ch):
    s=1
    for i in range (len(ch)-1):
        s*=10
    return s


def palin(ch):
    if len(ch)<=1:
        return True
    elif ch[0] != ch[-1]:
        return False
    else :
        return palin(ch[1:len(ch)-1])
    
print(palin("yahy"))
print(palin("radar"))
         


def puiss_rec(b,a,n):
    if n==1:
        return a
    else:
        return puiss_rec(b,b*a,n-1)
        
        


    




""""def remplir1():
    t=array([int]*5)
    for i i n range 4:
        t[i]=int(input("Donner  un nombre\n"))
    
    
def rec_t(T,n):
    if n==0:"""
        

    
    

    
    