#básico
frase = "Olá, tudo bemm?  ";
lista = ["ligar", "desligar",12, 3.2, True];

print(frase[0:2]);
print(lista[0:5:2]);
print(frase[::-1]);#inverte uma string

#operações

lista.append("Adicionando itens"); # adiciona um item na última posição
print(lista);
lista.remove("ligar"); #remove um item
print(lista);
lista.insert(0,"ligar2"); #add em uma posição especifica
print(lista);
lista[0]="desligar";
print(lista);
print(lista.count("desligar")); #conta o número de vezes q aparece esse item na lista

print(lista);
print(lista.pop()); # pega o último item e remove da lista
print(lista);
espaco=" ";
lista1=[lista[0],lista[1],"uma outra lista"];
print(espaco.join(lista1));
lista.clear(); #limpa lista
print(lista);


print(frase.lower());
print(frase.upper());
print(frase.swapcase());
print(frase.split(","));# separa string toda vez q tiver o elemento (",") e gera uma lista
print(list(frase));# cada caracter vira um item da lista
print(frase.startswith("Olá"));#imprime true caso a frase comece com esse caracter;
print(len(frase));
frase=frase.strip()#remove espaços antes ou depois da string
print(frase);
print(len(frase));

ate=frase.find("t");# informa a posição do caracter
depois=frase.find(" ",ate);# encontra um espaço após a posição do caracter "t"
print(frase[ate:depois]); # imprime a string "tudo";

#O seguinte exemplo usa %d para formatar um inteiro, %g para formatar um número de ponto flutuante, e %s para formatar uma string:
anos=30;
pais="Grécia";
frase2 ="Em %d anos a população da %s ira aumentar em %g milhões" %(anos,pais,2.2);
print(frase2);
