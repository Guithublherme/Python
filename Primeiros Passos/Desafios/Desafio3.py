
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


