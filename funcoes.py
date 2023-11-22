def incluir(vetor):
    pessoa = {}
    pessoa['nome'] = input("Informe nome: ")
    pessoa['email'] = input('Informe o e-mail: ')
    pessoa['telefone'] = input('Informe o telefone: ')

    vetor.append(pessoa)
    
def pesquisar(vetor, nomeBusca):
    posicao = -1
    encontrado=False
    for elemento in vetor:
        posicao =  posicao + 1
        if elemento["nome"].lower()== nomeBusca.lower():
          encontrado = True  
          break
        return posicao   
    if encontrado:
        return posicao
    else:
        return -1
      
                