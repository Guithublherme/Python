#Operadores lógicos e estruturas de decisões (IF e ELSE)

var_verdadeiro = True;
var_falso = False;

print(var_verdadeiro,type(var_falso));
print(not(var_falso) and var_verdadeiro);

#comparadores  ==  >  <  >=  <=  !=
#Estruturas de decisão

a = 10;
b = 32;
if a > b:
	print("a é maior que b");
elif a < b:
	print("a é menor que b");
else :
	print("a é igual a b");

'''
Exercicio: Programa que pergunte a idade, peso e altura
e decida se ela pode entrar no exercito.
Para entrar é preciso ter 18 anos ou mais,
ter mais de 60 kg e uma altura maior que 1,70 metros.
'''
print("-"*100);
print("-"*100);
print("Verifique se vc está apto a entrar no Exército");
idade=input("Qual sua idade? ");
altura=input("Qual sua altura? ");
peso=input("Qual seu peso? ");

if (int(idade)>=18) and (float(altura)>1.70) and (int(peso)>60):
	print("Você está apto");
else:
	print("Você não está apto");
print("-"*100);
print("-"*100);