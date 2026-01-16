texte1="abcde"
texte2="abcdEfgtidozpsdkopsf"

def inclus(a,b):
    a=set(a)
    b=set(b)
    for i in a :
        if i in b:
            continue
        else:
            return False
    return True



def verifier_entier_valide(var,inf,sup):
    return inclus(set(str(var)),'0123456789') and int(var)>inf and int(var)<sup


print(verifier_entier_valide("a",1,10))

