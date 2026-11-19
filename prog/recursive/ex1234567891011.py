def pgcd(a,b):
        if b==0:
            return a
        else :
            return pgcd(b,a%b)
        
        
print(pgcd(50,35))





def chaine(ch):
    if len(ch)<1:
        return ""
    else:
        return ch[len(ch)-1] + chaine(ch[:len(ch)-1])
    
print(chaine("yahya"))





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
    
print(chercher_ent(9897454,1))