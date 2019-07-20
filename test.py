from metodos import *

###################################################
##                                               ##                        
##   @author Victor jx                           ##
##   script creado solo para realizar pruebas    ##
##                                               ##
###################################################


variable = "13+23"
var =","


new = var.join(variable)
lista = new.split(",")


print (var.join(variable))
print(lista)

signo =""
num1 =""
num2 =""
# identificar signo y numeros
for a in lista:
    if ord(a) == 43 or ord(a) == 42 or ord(a) == 45:
        signo += a
    else:
        if signo == "":
            num1 += a
        else:
            num2 +=a
            
# obtener operacion

print(" ------------",signo) 
print("valor de a {} valor de b {}".format(num1,num2))

print("el resultado es ",operacion(signo,int(num1),int(num2)))


