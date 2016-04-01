from django.http import HttpResponse
from heapq import heappush, heappop

from .numeros import readFile
from .crono import cronometro

def heapsort(iterable):
    'Equivalent to sorted(iterable)'
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

def heap(r):
    name = r.GET.get('nombre')
    n = readFile(name)
    t = cronometro(heapsort)(n)
    return HttpResponse("el tiempo  ordenamiento de "+name+" números es: "+str(t)+" segundos")