"""
1. Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos.
"""

from operator import truediv


def maximo(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
print(maximo(2000.1,3))

"""
2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""
def maxitres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

print(maxitres(1123, 422, 222))
"""
4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def esvocal(caracter):
    lista_vocales = ['a','e','i','o','u']
    if caracter in lista_vocales:
        return True
    else:
        return False
print(esvocal('u'))
print(esvocal('b'))

"""
5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
def suma(lista):
    resultado = 0
    for n in lista:
        resultado = resultado + (n)
    
    print (resultado)


def multiplicar(lista):
    resultado = lista[0]
    i = 1
    while i in range(1, len(lista)):
        resultado = resultado * lista[i]
        i += 1
    print(resultado)

suma([2,2,2])
multiplicar([2,2,2])

"""
6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""


"""
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""


"""
8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""



"""
9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""


"""
10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
"""