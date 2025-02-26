def elefantes(n, i=1):
    if (i == n):
        return str(n) + " elefantes " + incomodam(n) + "muito mais"
    else:
        if(i == 1):
            return "Um elefante incomoda muita gente\n" + elefantes(n, i + 1)
        elif(n <= 0):
            return ""
        else:
            return str(i) + " elefantes " + incomodam(i) + "muito mais\n" + str(i) + " elefantes incomodam muita gente\n" + elefantes(n, i + 1)

def incomodam(n):
    return "incomodam " * n
