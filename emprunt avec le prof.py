from math import*
Co=float(input("la valeur initiale : "))
i=float(input("le taux d'interêt : "))
n=int(input("la période : "))
I=Co*i
Cn=Co*pow(1+i,n)
Ic=Cn-Co
R=(Ic/Co)*100
print("la valeur finale =", format(Cn,".2f"))
print("la valeur de l'intérêt simple =", format(I,".2f"))
print("la valeur de l'intérêt composé =", format(Ic,".2f"))
print("le taux de rendement =", R, "%")
for j in range(1,n):
    print("la période",j,":","l'annuités:", format(Co*pow(1+i,j),".2f"))

