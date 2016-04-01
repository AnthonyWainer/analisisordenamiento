from django.http import HttpResponse
from .numeros import readFile
from .crono import cronometro

def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

#alist = [54,26,93,17,77,31,44,55,20]
def quick(r):
    name = r.GET.get('nombre')
    alist = readFile(name)
    t = cronometro(quicksort)(alist)
    #print(alist)
    return HttpResponse("el tiempo  ordenamiento de "+name+" números es: "+str(t)+" segundos")