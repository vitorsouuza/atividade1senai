import random, os

esconde = random.randrange (0,50)

dificuldade = int(input(" 1-easy \n 2-medium \n 3-hard \n R: "))
acertou = False

if dificuldade == 1: 
 tentativas = 15
elif dificuldade == 2:
    tentativas= 10
else:
    tentativas = 5 
    
for x in range (0, tentativas) :
    print("voce tem " + str(x + 1) + " de " + str(tentativas) + " tentativas ")
    
    nt = int (input("informe um numero:"))
    if nt > esconde:
       print("esta mais a esquerda")
    elif nt < esconde:
       print("esta mais a direita")
    else:
       acertou = True 
       break
   
if acertou == False:
       print("voçe perdeu ele está na posição " + str(esconde))
else:
       print("achou!")       