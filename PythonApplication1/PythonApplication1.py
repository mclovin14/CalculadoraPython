import Calculadora;

print("Digite um número: ");
numero1 = int(input());
print("Digite um número: ");
numero2 = int(input());
print("Digite a operação que queira realizar com estes dois números: ");
tipo = input();
tipo = tipo.upper();
Calculadora.Calculadora.calcular(tipo, numero1, numero2);   


