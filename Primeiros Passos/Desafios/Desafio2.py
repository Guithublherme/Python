
data=input();
A = (data[0:2]); # dia
B = (data[3:5]); # mês
C = (data[6:8]); # ano

print(B,A,C,sep="/"); # MM/DD/AA
print(C,B,A,sep="/"); # AA/MM/DD
print(A,B,C,sep="-"); # DD-MM-AA