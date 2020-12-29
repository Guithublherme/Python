#aula 1 váriaveis, tipos, entradas e saídas, operadores matemáticos

#saídas

print("Olá mundo!");

print('Segundo print\noutra linha\t Usando o tab');

#variáveis

Nome = "Guilherme";
idade = 27;
altura = 1.75;
print(Nome);
print("Nome:"+ Nome); #concatena Strings apenas
print("Nome:",Nome,"tem",idade,"anos");
tipoNome= type(Nome);
tipoIdade= type(idade);
tipoAltura= type(altura);
print(tipoNome,tipoIdade,tipoAltura); #str , int, float

#entradas
Nome = input("Escreva seu nome: ");
idade = input("Digite sua idade: ");
print("Nome:",Nome,"tem",idade,"anos");

#Operações matemáticas

num1 = 42;
num2 = 2;
num3 = 3.0;
resultado = num2 + num1 / (num3**num2)**(1/2);

print(resultado);