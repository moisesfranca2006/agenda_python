salario=float(input("Digite o valor do salario="))
cargo=int(input("Digite o codigo do Funcionario="))
nomeCargo=""
match cargo:
    case 100:
        percentual=20
        nomeCargo="Auxiliar Administrativo" 
    case 101:
        percentual=15
        nomeCargo="Engenheiro"
    case 102:
        percentual=10
        nomeCargo="gerente"
    case _:   
        percentual = 0
        nomeCargo = "Cargo Inválido"

reajuste = salario * (percentual/100)

novo_salario = salario + reajuste

print(f"Cargo: {nomeCargo}\nSalário: {salario:.2f}\nReajuste: {reajuste:.2f}\nNovo Salário: {novo_salario:.2f}")