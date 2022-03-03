Formas de fatiamento :

#   Ele mostra as letras até o numero da chave ATENÇÃO AOS 2 PONTOS -->  :

                                    frase = curso em vídeo

                    [C u r s o   e m   v í  d  e  o     P  y  t   h  o  n ]
                    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Frase[9] -                             v                    #
Frase[9:13]                            v  i  d  e           #
Frase[9:21]                            v  i  d  e  o    p   y  t  h  o  n
                                                            #
                                                            #
Frase[9:21:2]                          v     d     o    p      t     o
                                                            #
                                                            #
Frase[:5]            c u r s o                              #
Frase[15:]                                              p   y   t  h  o  n
Frase[9::3]                            v        e       p           h
___________________________________________________________________________________________________________

                                    FUNÇÕES         IMPORTANTISSIMAS

len = comprimento (lenght)

            len(frase) = 21 caracteres em (curso em vídeo)
_____________________________________________________________________________________________________________
frase.count('o')   <----- o parenteses determina a string e o .count determina o comando de contar
frase.count('o', 0, 13)  <------------ ELE CONTA JÁ FATIANDO A STRING DO ZERO AO 12 (O ULTIMO VALOR O PYTHON IGNORA)
frase.find('deo')      <----------- ELE VAI PROCURAR NA STRING "" ONDE COMEÇOU   "DEO"  NO CODIGO
frase.find('Android') <-------- ELE RETORNA -1 NO RESULTADO SIGNIFICANDO QUE NÃO ENCONTROU A STRING NO CODIGO
'Curso' in frase       <----- True
_________________________________    TRANSFORMAÇÃO ______________________________________________________________
frase.replace('Python', 'Android')  <----      ELE VAI SUBSTITUIR PYTHON POR ANDROID
frase.strip()  <---- REMOVE OS ESPAÇOS INUTEIS NO (INICIO E NO FINAL) DA STRING
frase.rstrip() <---- REMOVE OS ESPAÇOS COMEÇANDO PELA (DIREITA) da STRING
frase.lstrip() <---- REMOVE OS ESPAÇOS COMEÇANDO PELA (ESQUERDA) DA STRING

frase.upper()  < ----- ELE VAI DEIXAR TUDO EM MAIUSCULO, () É UM METODO
frase.lower() < ------ PYTHON VAI DEIXAR A STRING EM MINUSCULO
frase.capitalize() <----- ELE VAI DEIXAR SÓ A PRIMEIRA LETRA DA STRING INTEIRA EM MAIUSCULO
frase.title()     <------ TRANSFORMA TODAS AS LETRAS APÓS O ESPAÇO EM MAIUSCULO

____________________________ DIVISÃO ___________________________________
frase.split()  <---- ESTUDAR SOBRE OUTRAS FUNCIONALIDADES NOS PARENTESES DO COMANDO SPLIT

___________________________ JUNÇÃO _______________________________________
'-'.join(frase) <------- ELE JUNTA DEPOIS DO SPLIT COLOCANDO  -  ONDE ERA OS ESPAÇOS E UNINDO A STRING NOVAMENTE






















