vetor =[]

media= 0
soma=0
while True:
    numero=int(input("Digite o Numero="))
    if numero==0:
        break
    vetor.append(numero)
    media=media+1
    soma=soma+numero
#for elemento in vetor:
media=soma/media 
#print(elemento, soma, media)
    
print(soma, media)
 