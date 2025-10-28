# calculadora_simple.py
# Autor: Arnau Pardal
# Descripcion: calculadora basica en PythonFinalizationError

def sumar(a,b):
    return a +b

def restar(a,b):
    return a-b

def multi(a,b):
    return a*b
def divi(a,b):
    if b == 0:
        return "division por 0"
    else:
        return a/b

def potencia(a,b):
    return a^b

def main():
    print('Calculadora simple')
    x = float('Introduce un numero')
    y = float('Introduce un numero')

    print(f'Sumar {sumar(x,y)}')
    print(f'Restar {restar(x,y)}')
    print(f'Multiplicar {multi(x,y)}')
    print(f'Dividir {divi(x,y)}')
    print(f'Potencia {potencia(x,y)}')
    
if __name__ == '__main__':
    main()