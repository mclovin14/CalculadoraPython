import sys;
class Calculadora(object):
    def _init_(self):
        self = self;

    def calcular(tipo, a, b):
        if tipo == 'A':
            print("O resultado é:", a + b);
        elif tipo == 'S':
            print("O resultado é:", a - b);
        elif tipo == 'M':
            print("O resultado é:", a * b);
        elif tipo == 'D':
            if a == 0 or b == 0:
                print("Impossivel realizar essa divisão.");
            else:
                print("O resultado é ", a / b);
        else:
            sys.exit;