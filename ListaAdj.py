def criar_grafo():
    """
    Retorna um novo grafo vazio.
    Passos:
    1. Criar um dicionário vazio: {}
    2. Retornar o dicionário (representa o grafo)
    """
    
    return({})


def inserir_vertice(grafo: dict, vertices:list):
    """
    Insere um vértice no grafo, sem arestas iniciais.
    Passos:
    1. Verificar se 'vertice' já é chave em grafo.
    2. Se não for, criar entrada grafo[vertice] = []
    3. Se já existir, não fazer nada (ou avisar)
    """
    for vertice in vertices:
        if vertice in grafo.keys():
            return "Vétice já inserida"
    
        grafo[vertice] = []
        
    return(grafo)
    


def inserir_aresta(grafo: dict, origem, destino, nao_direcionado=False):
    """
    Adiciona aresta entre origem e destino.
    Passos:
    1. Garantir que 'origem' e 'destino' existam no grafo (inserir se necessário).
    2. adicionar destino como vizinho de origem (append).
    3. Se for Nâo Direcionado, também:
         - adicionar origem como vizinho de destino
    """
    if (origem and destino) in grafo.keys():
        if nao_direcionado == False:
            grafo[origem].append(destino)
        else:
            grafo[origem].append(destino)
            grafo[destino].append(origem)
        
    return(grafo)

def vizinhos(grafo: dict, vertice):
    """
    Retorna a lista de vizinhos de 'vertice'.
    Passos:
    1. Se 'vertice' estiver em grafo, retornar grafo[vertice] (lista).
    2. Se não existir, retornar lista vazia ou sinalizar erro.
    """
    if vertice in grafo.keys():
        print(grafo[vertice])
    else:
        print(f"O vertice {vertice} não existe no grafo")

def listar_vizinhos(grafo, vertice):
    """
    Função semântica: imprimir/retornar os vizinhos de 'vertice'.
    Passos:
    1. Obter lista = vizinhos(grafo, vertice)
    2. Retornar/imprimir essa lista (ou informar que o vértice não existe)
    """
    try:
        print(f'{vertice}:{grafo[vertice]}')
    except Exception as e:
        print(e)

def exibir_grafo(grafo:dict):
    """
    Exibe o grafo em forma legível (lista de adjacência).
    Passos:
    1. Para cada vertice em ordem
         - imprimir: vertice -> vizinhos
    """
    for key in grafo.keys():
        string = f"{key} -> " 
        string += ', '.join(grafo[key])
        print(string)

def remover_aresta(grafo:dict, origem, destino, nao_direcionado=False):
    """
    Remove a aresta entre origem e destino.
    Passos:
    1. Verificar se 'origem' existe; se não, terminar.
    2. Se destino estiver em grafo[origem], remover essa ocorrência.
    3. Se for não direcionado, também:
         - verificar se 'destino' existe e remover 'origem' de grafo[destino] se presente.
    """
    if origem in grafo.keys() and destino in grafo[origem]:
        if nao_direcionado == False:
            grafo[origem].remove(destino)
        else:
            grafo[destino].remove(origem)
                
        return(grafo)


def remover_vertice(grafo:dict, vertice, nao_direcionado=True):
    """
    Remove um vértice e todas as arestas que o tocam.
    Passos:
    1. Verificar se 'vertice' existe em grafo; se não, terminar.
    2. Para cada outro vertice no grafo:
         - se 'vertice' estiver na lista de vizinhos, remover essa aresta.
    3. Remover o vertice do grafo
    4. Opcional: retornar confirmação/erro.
    """
    if vertice in grafo.keys():
        grafo.pop(vertice)
        for i in grafo:
            if vertice in grafo[i]:
                grafo[i].remove(vertice)
            
        return(grafo)


def existe_aresta(grafo, origem, destino):
    """
    Verifica se existe aresta direta origem -> destino.
    Passos:
    1. Verificar se 'origem' é chave no grafo.
    2. Retornar True se 'destino' estiver em grafo[origem], caso contrário False.
    """
    if origem in grafo.keys() and destino in grafo[origem]:
        return True
    else:
        return False

def grau_vertices(grafo):
    """
    Calcula e retorna o grau (out, in, total) de cada vértice.
    Passos:
    1. Inicializar um dict de graus vazia
    2. Para cada vertice, colocar no dict uma estrutura com in, out e total zerado
    3. Para cada u em grafo:
         - out_degree[u] = tamanho de vizinhos
         - para cada v em grafo:
            - verificar se u está na lista de vizinho de v,
            - caso esteja, adicionar +1 para o grau de entrada de u
    4. Calcular o grau total somando entrada + saida
    5. Retornar uma estrutura contendo out,in,total por vértice (ex: dict de tuplas).
    """
    graus = {}

    for vertice in grafo:
        graus[vertice] = {"din":0, "dout":0, "total":0}

    for u in grafo:
        graus[u]["dout"] = len(grafo[u])

        for v in grafo:
            if u in grafo[v]:
                graus[u]["din"] += 1

    for vertice in grafo:
        graus[vertice]["total"] = graus[vertice]["din"] + graus[vertice]["dout"]
    
    return graus


def percurso_valido(grafo:dict, caminho:list):
    """
    Verifica se uma sequência específica de vértices (caminho) é válida:
    i.e., se existem arestas consecutivas entre os nós do caminho.
    Passos:
    1. Se caminho tiver tamanho < 2, retornar True (trivial).
    2. Para i de 0 até len(caminho)-2:
         - origem = caminho[i], destino = caminho[i+1]
         - se não existe_aresta(grafo, origem, destino): retornar False
    3. Se todas as arestas existirem, retornar True.
    """
    if len(caminho) < 2:
        return True
    
    for i in range(len(caminho)-1):
        origem = caminho[i]
        destino = caminho[i+1]

        if destino not in grafo[origem]:
            return False
        
        else:
            return True



def main():
    """
    Crie um menu onde seja possível escolher qual ação deseja realizar
    ex:
        1 - Mostrar o Grafo
        2 - inserir vertice
        3 - inserir aresta
        4 - remover vértice.
        ....
    """
    grafo = criar_grafo()
    while True:
        opcoes = {
            '1':'Mostrar grafo',
            '2':'Inserir vertice',
            '3':'Inserir aresta',
            '4':'Remover vertice',
            '5':'Remover aresta',
            '6':'Listar vizinhos',
            '7':'Verificar existência de vertice',
            '8':'Verificar existencia de aresta',
            '9':'Verificar grau dos vértices',
            '10':'Avaliar percurso'
            }

        for opcao in opcoes:
            print(opcao, opcoes[opcao])
    
        escolha = str(input("Insira uma opção: "))

        if escolha == '1':
            exibir_grafo(grafo)
        elif escolha == '2':
            inserir_vertice(grafo, input("\nVertice a ser adicionado: "))
        elif escolha == '3':
            exibir_grafo(grafo)
            origem = input("\nVertice origem: ")
            destino = input("\nVertice destino: ")
            direcionado = bool(input("\nÉ direcionada? (True ou False): "))
            inserir_aresta(grafo, origem, destino, direcionado)
        elif escolha == '4':
            listar_vizinhos(grafo)
            remover_vertice(grafo, input("\nVertice a ser removido: "))
        elif escolha == '5':
            listar_vizinhos(grafo)
            remover_aresta(
                grafo,
                input("Vertice origem"),
                input("Vertice destino"),
                input("É direciona? (True ou False)")
                )
        elif escolha == '6':
            listar_vizinhos(grafo, input("\nVertice para consultar os vizinhos: "))
        elif escolha == '7':
            if vizinhos(grafo, "\nVertice a ser verificado: "):
                print(True)
        elif escolha == '8':
            if existe_aresta(
                grafo,
                input("Vertice origem: "),
                input("Vertice destinio")
            ):
                print("Aresta valida")
            else:
                print("Aresta inexistente")
        elif escolha == '9':
            graus = grau_vertices(grafo)
            for grau in graus:
                print(grau, graus[grau])
        elif escolha == '10':
            percurso = input("Percurso a ser verificado (Separe as vétices co , )").split(',')
            if percurso_valido(grafo, percurso):
                print("O percurso é valido")
            else:
                print("O percurso não é valido")
    pass


if __name__ == "__main__":
    main()