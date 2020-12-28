# Meteoros

# Em noites sem nuvens pode-se muitas vezes observar pontos brilhantes no céu que se deslocam com grande velocidade, e em poucos segundos desaparecem de vista: são as chamadas estrelas cadentes, ou meteoros. Meteoros são na verdade partículas de poeira de pequenas dimensões que, ao penetrar na atmosfera terrestre, queimam-se rapidamente (normalmente a uma altura entre 60 e 120 quilômetros). Se os meteoros são suficientemente grandes, podem não queimar-se completamente na atmosfera e dessa forma atingem a superfície terrestre: nesse caso são chamados de meteoritos.

# Zé Felício é um fazendeiro que adora astronomia e descobriu um portal na Internet que fornece uma lista das posições onde caíram meteoritos. Com base nessa lista, e conhecendo a localização de sua fazenda, Zé Felício deseja saber quantos meteoritos caíram dentro de sua propriedade. Ele precisa de sua ajuda para escrever um programa de computador que faça essa verificação automaticamente.

# São dados:

# • uma lista de pontos no plano cartesiano, onde cada ponto corresponde à posição onde caiu um meteorito;

# • as coordenadas de um retângulo que delimita uma fazenda. As linhas que delimitam a fazenda são paralelas aos eixos cartesianos. Sua tarefa é escrever um programa que determine quantos meteoritos caíram dentro da fazenda (incluindo meteoritos que caíram exatamente sobre as linhas que delimitam a fazenda).

# Entrada
# Seu programa deve ler vários conjuntos de testes. A primeira linha de um conjunto de testes quatro números inteiros X1 , Y1 , X2 e Y2, em que (0 ≤ Y2 < Y1 ≤ 10.000) e (0 ≤ X1 < X2 ≤ 10.000), onde (X1 , Y1 ) é a coordenada do canto superior esquerdo e (X2 , Y2 ) é a coordenada do canto inferior direito do retângulo que delimita a fazenda. A segunda linha contém um inteiro, N (0 ≤ N ≤ 10.000), que indica o número de meteoritos. Seguem-se N linhas, cada uma contendo dois números inteiros X (0 ≤ X ≤ 10.000) e Y (0 ≤ Y ≤ 10.000), correspondendo às coordenadas de cada meteorito. O final da entrada é indicado por X1 = Y1 = X2 = Y2 = 0.

# Saída
# Para cada conjunto de teste da entrada seu programa deve produzir duas linhas na saída. A primeira linha deve conter um identificador do conjunto de teste, no formato “Teste n”, onde n é numerado a partir de 1. A segunda linha deve conter o número de meteoritos que caíram dentro da fazenda.



nz=0;
nz1=[];
num1=[];
while(True):

	teste = input();
	
	y=0;
	X1="";Y1="";X2="";Y2="";
	for x in range (0,len(teste)):
		if(teste[x]==" "):
			#print("leu um espaço");
			y=y+1;
			#print(y);
		else:
			if(y==0):
				X1=X1+teste[x];
			elif(y==1):
				Y1=Y1+teste[x];
			elif(y==2):
				X2=X2+teste[x];
			elif(y==3):
				Y2=Y2+teste[x];	
		
	else:
		
		x1=int(X1);
		x2=int(X2);
		y1=int(Y1);
		y2=int(Y2);
	
	if (x1==0 and x2==0 and y1==0 and y2==0 ):
		break

	valor="";	
	N=input();
	for x in range (0,int(N)):
		valor = valor+input()+" ";
	
	
	valor2=valor.split();
	
	z=0;
	X=[]* 10;
	Y=[]* 10;
	
	
	
	j=0;
	k=0;
	for x in range (0,len(valor2)):
	
		if ( x%2 == 0): #par...X
			X.append(int(valor2[x]));
		else:  # impar....Y
			Y.append(int(valor2[x]));
	
	xx=(X);
	yy=(Y);
	num=0;
	
	
	for y in range(0,int(N)):
		
		if ((int(xx[y])>=x1) and (int(xx[y])<=x2) and (int(yy[y])<=y1) and (int(yy[y])>=y2)):
			num=num+1;#print("passou por aqui");
	nz=nz+1;
	nz1.append(nz);
	num1.append(num);

#####fim do while
for x in range(0,len(nz1)):
	print("Teste",nz1[x]);
	print(num1[x]);


