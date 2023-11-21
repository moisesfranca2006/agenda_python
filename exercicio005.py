codigo=int(input("Digite o codigo do Funcionario="))
salario=float(input("Digite o valor do salario="))
salariajustado=float()
if codigo==100:
   salarioajustado=salario*20/100
   salarioajustado=salarioajustado+salario
   print("Auxiliar administrativo Salário ajustado=", salarioajustado)
elif codigo==101:
   salarioajustado=salario*15/100
   salarioajustado=salarioajustado+salario
   print("Engenheiro Salário ajustado=", salarioajustado)
elif codigo==102:
   salarioajustado=salario*10/100
   salarioajustado=salarioajustado+salario
   print("Gerente salário ajustado=", salarioajustado)
else:
   print("Fim!")

