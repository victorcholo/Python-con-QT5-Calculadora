# @author Victor jx


def signo_num(lista):
    for a in lista:    
        if ord(a) == 43 or ord(a) == 42 or ord(a) == 45:
            signo += a
        else:
            if signo == "":
                num1 += a
            else:
                num2 +=a


def operacion(signo,num1,num2):
    if signo == "+":
        return float(num1)+float(num2)
    elif signo == "-":
        return float(num1)-float(num2)
    elif signo == "*":
        return float(num1)*float(num2)
    elif signo == "/":
        return float(num1)/float(num2)


    
