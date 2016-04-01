elementos = [1,3,5,4,7,9,8,6]
from django.http import HttpResponse
from .numeros import readFile
from .crono import cronometro

def burbuja(elementos):
    numero = len(elementos)
    i= 0
    while (i < numero):
        j = i
        while (j < numero):
            if(elementos[i] > elementos[j]):
                temp = elementos[i]
                elementos[i] = elementos[j]
                elementos[j] = temp
            j= j+1
        i=i+1

def burbu(r):
    name = r.GET.get('nombre')
    e = readFile(name)
    t = cronometro(burbuja)(e)
    #print(alist)
    return HttpResponse("el tiempo  ordenamiento de "+name+" números es: "+str(t)+" segundos")

    #for elemento in elementos:
        #print(elemento)