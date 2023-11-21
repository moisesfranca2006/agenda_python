print("Faça seu pedido de acordo com o Menu")
print("Produto --------- Código------Preço")
print("Cachorro Quente     100      R$1,20")
print("Brauny Simples      101      R$1,30")
print("Bauru com Ovos      102      R$1,60")
print("Hanburgue           103      R$1,20")
print("Sheesburgue         104      R$1,30")
print("Refrigerante        105      R$1,00")
codigo=int(input('Digite o codigo do Pedido='))
quantidade=int(input('Quantidade de pedido='))
item=" "
valor=float()
total=float()
if codigo==100:
    item="Cachorro quente"
    valor=1.20
    valor=valor*quantidade
    total=valor
elif codigo==101:
    item="Brauny Simples"
    valor=1.30
    valor=valor*quantidade
else:
    print("Fim")
print("Pedido do Cliente",item,codigo,total) 
   