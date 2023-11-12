def est_Bissextile(annee):
    if ( annee % 4 == 0 and annee % 100 != 0 ) or (annee % 400 == 0):
        return True
    else :
        return False
def Annee_bissextile(siecle):
    for i  in range ((siecle-1)*100,(siecle)*100+1):
        
        if est_Bissextile(siecle) == True:
            
            return i       

def remplir_matrice(N, P):
    if N <= 0 or P <= 0 or N > 10 or P > 10:
        print("Les valeurs de N et P doivent être > 0 et ≤ 10.")
        return

    matrice = [[0] * P for _ in range(N)]

    valeur = 1
    for i in range(N):
        for j in range(P):
            matrice[i][j] = valeur
            valeur += 1

    print("Affichage normal:")
    for i in range(N):
        print(matrice[i])

    print("\nAffichage alternatif:")
    for i in range(N):
        if i % 2 == 0:
            print(matrice[i])
        else:
            reversedList = []
            for j in range(len(matrice[i])-1,-1,-1):
                reversedList.append(matrice[i][j])
            
            print(reversedList)     
N = int(input("Saisire l' entier N :"))
P = int(input("Saisire l' entier P :"))
remplir_matrice(N,P)    
             


tab=[]
n=int(input("entrer la taille du tableau : "))
for i in range(0,n):
    tab.append(int(input("entrer un entier :")))
print(tab)
case1=int(input("entrer la première case du tableau"))
case2=int(input("entrer la deuxième case du tableau"))
tab1=[]
for i in range(case2-case1+1) :
    tab1.append(tab[case1-1+i])
print("la somme est : ", sum(tab1))


def NbCMIn(Pass):
    c = 0
    for i in Pass :
        if Pass.islower() == True :
            c += 1
    return c
def NbCMaj(Pass):
    c = 0 
    for i in Pass :
        if Pass.islower() == True:
            c += 1 
    return c 
def NbCAlpha(Pass):
    c = 0
    for i in Pass :
        if Pass.isalpha() == False :
            c += 1
    return c 
def LongMaj(Pass):
    longest_sequence = ""
    for i in Pass:
        if i.isupper() == True:
            longest_sequence += i
    return longest_sequence
def LongMin(Pass):
    longest_sequence = ""
    for i in Pass :
        if i.islower():
            longest_sequence += i
    return longest_sequence
def Bonus(Pass):
    bonus = 0 
    bonus = (len(Pass) * 4) + ((len(Pass) - NbCMaj(Pass)) * 2 ) + (( len(Pass) - NbCMIn(Pass)) * 3) + NbCAlpha(Pass) * 5 
    return bonus
def Malus(Pass) :
    malus = (len(LongMin(Pass))*2) + (len(LongMaj(Pass))*2)
    return malus
def Score(Pass):
    score = Bonus(Pass) + Malus(Pass) 
    return score

PassWord = str(input("Entrer votre mot de pass :"))
if Score(PassWord) < 20 :
    print(f" Le {PassWord} est très faible ")
elif 20 <= Score(PassWord) < 40 :
    print(f" Le {PassWord} est faible ")
elif  40 <= Score(PassWord) < 80 :
    print(f" Le {PassWord} est fort ")
else :
    print(f" Le {PassWord} est très fort ")

