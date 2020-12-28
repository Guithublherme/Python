X = 0;
while (X==0):
	try:
		#A= input("Digite dois números inteiros: \n");
		A= input();
		B= input();
		X= int(A) + int(B);
		print("X = "+str(X)+"\n");
	except: 
		print("Entre com um inteiro");



