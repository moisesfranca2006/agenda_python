from funcoes import incluir, pesquisar,listar


def menu():
    print("1 - Cadastro")
    print("2 - Pesquisa pelo nome")
    print('3 - Listar')
    print('4 - Alterar')
    print('5 - Excluir')
    print('9 - Sair')
    
agenda = []

while True:
   menu()
   opcao = int( input('Informe a opção: '))
   if opcao == 1: 
        incluir(agenda)
       
   elif opcao == 2:
        nomeBusca = input('Informe o nome para busca: ')
        indice = pesquisar(agenda,nomeBusca)
        if indice != -1:
           print(f"""{agenda[indice]['nome']}
                 
                 - {agenda[indice]['email']}-
                  {agenda[indice]['telefone']}""")
        else:
            print("Contato nao encontrado")   
   elif opcao == 3:
       listar(agenda)
   elif opcao == 4:
        nomeBusca = input('Informe o nome para busca: ')    
        posicao = pesquisar(agenda, nomeBusca)
        
        if posicao != -1:
            agenda[posicao]['nome'] = input("Informe o nome: ")
            agenda[posicao]['email'] = input("Informe o e-mail: ")
            agenda[posicao]['telefone'] = input("Informe o telefone: ")
        else:
            print("Contato nao encontrado")     
   elif opcao == 5:
        nomeBusca = input('Informe o nome para busca: ')    
        posicao = pesquisar(agenda, nomeBusca)
        
        if posicao != -1:
            agenda.pop(posicao)
        else:
            print("Contato nao encontrado") 
               
   elif opcao == 9:
        break
   else:
        print("Opção Inválida.")