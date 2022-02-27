"""
## GENERADOR DE NUMEROS PSEUDOALEATORIOS LINEAL CONGRUENCIAL
## x0 -> semilla
## a -> multiplicador constante
## c -> incremento
## m -> modulo
## r -> numero aleatorio
## i -> numero de iteraciones que queremos generar
"""
def linearConguencial (x0, a, c, m):
    for j in range(6):
        x1 = ((a*x0)+c)%m
        x0 = x1
        r = x1/m
        print(r)
"""
## GENERADOR DE NUMEROS PSEUDOALEATORIOS MULTIPLICATIVO LINEAL CONGRUENCIAL
## x0 -> semilla y un numero inpar
## a -> multiplicador constante
## m -> magnitud del modulo
## r -> numero aleatorio
## n -> mayor a 0
"""
def MultiplicativeLC(x0,a,m):
    for j in range(3):
        n=1
        x1 = (a*x0)%m
        x0 = x1
        print(r)

if __name__ == '__main__':
    """linearConguencial(37,19,33,100)"""
    MultiplicativeLC(1,5,32)