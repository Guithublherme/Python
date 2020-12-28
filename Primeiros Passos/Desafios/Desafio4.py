
valor=(input());

valor2=valor.split();

A1=float(valor2[0]);
A2=float(valor2[1]);
A3=float(valor2[2]);

if (A1>A2) and (A1>A3):
	A=A1;
	B=A2;
	C=A3;


elif (A2>A1) and (A2>A3):
	A=A2;
	B=A1;
	C=A3;

else:
	A=A3;
	B=A1;
	C=A2;
	
if ((A)>=((B)+(C))):
	print("NAO FORMA TRIANGULO");

elif ((A**2)==((B**2)+(C**2))):
	print("TRIANGULO RETANGULO");

elif ((A**2)>((B**2)+(C**2))):
	print("TRIANGULO OBTUSANGULO");
	if (A==B==C):
		print("TRIANGULO EQUILATERO");
	elif (A==B or A==C or B==C):
		print("TRIANGULO ISOSCELES");

elif ((A**2)<((B**2)+(C**2))):
	print("TRIANGULO ACUTANGULO");
	if (A==B==C):
		print("TRIANGULO EQUILATERO");
	elif (A==B or A==C or B==C):
		print("TRIANGULO ISOSCELES");
