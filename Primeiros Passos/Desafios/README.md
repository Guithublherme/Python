# Desafios

 ## Desafio 1

Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

> ### Entrada
> A entrada contém 2 valores inteiros.

> ### Saída
> Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha.

 ## Desafio 2
 
Um programa com as seguintes características:

> Leia uma data no formato DD/MM/AA;
> Imprima a data no formato MM/DD/AA;
> Imprima a data no formato AA/MM/DD;
> Imprima a data no formato DD-MM-AA.

 ## Desafio 3

Zé Felício é um fazendeiro que adora astronomia e descobriu um portal na Internet que fornece uma lista das posições onde caíram meteoritos. Com base nessa lista, e conhecendo a localização de sua fazenda, Zé Felício deseja saber quantos meteoritos caíram dentro de sua propriedade. Ele precisa de sua ajuda para escrever um programa de computador que faça essa verificação automaticamente.

São dados:

- uma lista de pontos no plano cartesiano, onde cada ponto corresponde à posição onde caiu um meteorito;

- as coordenadas de um retângulo que delimita uma fazenda. As linhas que delimitam a fazenda são paralelas aos eixos cartesianos. Sua tarefa é escrever um programa que determine quantos meteoritos caíram dentro da fazenda (incluindo meteoritos que caíram exatamente sobre as linhas que delimitam a fazenda).

> Entrada

> Seu programa deve ler vários conjuntos de testes. A primeira linha de um conjunto de testes quatro números inteiros X1 , Y1 , X2 e Y2, em que (0 ≤ Y2 < Y1 ≤ 10.000) e (0 ≤ X1 < X2 ≤ 10.000), onde (X1 , Y1 ) é a coordenada do canto superior esquerdo e (X2 , Y2 ) é a coordenada do canto inferior direito do retângulo que delimita a fazenda. A segunda linha contém um inteiro, N (0 ≤ N ≤ 10.000), que indica o número de meteoritos. Seguem-se N linhas, cada uma contendo dois números inteiros X (0 ≤ X ≤ 10.000) e Y (0 ≤ Y ≤ 10.000), correspondendo às coordenadas de cada meteorito. O final da entrada é indicado por X1 = Y1 = X2 = Y2 = 0.

> Saída

> Para cada conjunto de teste da entrada seu programa deve produzir duas linhas na saída. A primeira linha deve conter um identificador do conjunto de teste, no formato “Teste n”, onde n é numerado a partir de 1. A segunda linha deve conter o número de meteoritos que caíram dentro da fazenda.


 ## Desafio 4
 
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

> se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO

> se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO

> se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO

> se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO

> se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO

> se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
