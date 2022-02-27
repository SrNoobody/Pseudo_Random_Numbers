import math
"""
## GENERADOR DE NUMEROS PSEUDOALEATORIOS LINEAL CONGRUENCIAL
## x0 -> semilla
## a -> multiplicador constante
## c -> incremento
## m -> modulo
## r -> numero aleatorio
## i -> numero de iteraciones que queremos generar
"""
def linearCongruencial (x0, a, c, m):
    for j in range(6):
        x1 = ((a*x0)+c)%m
        x0 = x1
        r = x1/m
        print(r)
"""
## GENERADOR DE NUMEROS PSEUDOALEATORIOS LINEAL CONGRUENCIAL v2
## x0 -> semilla
## a -> multiplicador constante
## k -> entero
## m -> modulo
## r -> numero aleatorio
## c -> relative prime with m
"""
def linearC (x0, k, g, c):
    m = pow(2,g)
    a = 1 + (4 * k)
    for j in range(8):
        aux = c +(a * x0)
        x1 = aux%m
        x0 = x1
        r = x1/(m-1)
        print(r)
"""
## GENERADOR DE NUMEROS PSEUDOALEATORIOS MULTIPLICATIVO LINEAL CONGRUENCIAL
## x0 -> semilla y un numero inpar entero
## k -> numero entero
## g -> numero entero
## r -> numero aleatorio
## n -> iteraciones 
## m -> 2^g
"""
def MultiplicativeLC(x0,k,g):
    m = pow(2, g)
    a = 5 + (8 * k)
    aux = m-1
    for j in range(8):
        x1 = (a*x0)%m
        x0=x1
        r = x1/(aux)
        print(r)
"""
## GENERADOR ADITIVO CONGRUENCIAL
## x1 -> semilla 
## x2 -> numero entero
## x3 -> numero entero
## m -> modulo
## r -> numero aleatorio resultante
"""
def AdditiveCGenerator(x1,x2,x3,m):
    for i in range(5):
        xi = (x3 + x1)%m
        x1 = x2
        x2 = x3
        x3 = xi
        r =  xi/(m-1)
        print(r)

if __name__ == '__main__':
    ##linearCongruencial(6,19,33,100)
    ##MultiplicativeLC(17,2,5)
    ##AdditiveCGenerator(65,89,98,100)
    linearC(6,3,3,7)