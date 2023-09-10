from math import*
Co=float(input("le capital initial:" ))
i=float(input("le taux d'interêt: "))
n=int(input("la periode ou durée: "))
C=Co*(1+i)
Cn=Co*pow(1+i,n)
Ia=Co*i
In=Cn-Co
R=(In/Co)*100
print("valeur finale à interêt simple=", C)
print("valeur finale à interêt composé=",Cn)
print("interêt simple=", Ia)
print("Interêt composé=",In)
print("taux de rendement=",R,"%")
print("le tableau d'amortissement")
for k in range(1,n):
    print("periode:",k,"Amortisement:",Co/n,"l'intérêt cumulé",(Co*pow(1+i,k)-Co),"l'annuités:",Co*pow(1+i,k))
X=input("saisir O si c'est validé ou N invalidé")
if X.upper()=="O":
    print("Accord validé")
else:
    print("Accord invalidé")

    