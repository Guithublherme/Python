# O seu professor gostaria de fazer um programa com as seguintes características:

# Leia uma data no formato DD/MM/AA;
# Imprima a data no formato MM/DD/AA;
# Imprima a data no formato AA/MM/DD;
# Imprima a data no formato DD-MM-AA.

data=input();
A = (data[0:2]); # dia
B = (data[3:5]); # mês
C = (data[6:8]); # ano

print(B,A,C,sep="/"); # MM/DD/AA
print(C,B,A,sep="/"); # AA/MM/DD
print(A,B,C,sep="-"); # DD-MM-AA