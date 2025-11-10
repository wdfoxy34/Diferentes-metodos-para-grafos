class Grafo:
    def __init__(self):
        """
        Cria e retorna uma matriz de adjacência vazia e uma lista de vértices.

        Passos:
        1. Criar uma lista vazia chamada matriz (para armazenar as conexões).
        2. Criar uma lista vazia chamada vertices (para armazenar os nomes dos vértices).
        3. Retornar (matriz, vertices). <- n tem pq, tá dentro da classe
        """
        self.matriz = []
        self.vertices = []

    def indentificar_index(self, *args):
        response = {}

        for arg in args:
            if arg in self.vertices:
                response[arg] = self.vertices.index(arg)

        return response

    def inserir_vertice(self, vertice):
        """
        Adiciona um novo vértice ao grafo.

        Passos:
        1. Verificar se o vértice já existe em 'vertices'.
        2. Caso não exista:
            - Adicionar o vértice à lista 'vertices'.
            - Aumentar o tamanho da matriz:
                a) Para cada linha existente, adicionar um valor 0 no final (nova coluna).
                b) Adicionar uma nova linha com zeros do tamanho atualizado.
        """
        if vertice in self.vertices:
            print(f"Vértice '{vertice}' já existe.")
            return

        self.vertices.append(vertice)

        for i in self.matriz:
            i.append(0)

        #nova linha para o vertice
        self.matriz.append([0] * len(self.vertices))
        print(f"Vértice '{vertice}' adicionado com sucesso.")
            

    def inserir_aresta(self, origem, destino, nao_direcionado=False):
        """
        Adiciona uma aresta entre dois vértices.

        Passos:
        1. Garantir que 'origem' e 'destino' existam em 'vertices':
            - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
        2. Localizar o índice da origem (i) e do destino (j).
        3. Marcar a conexão na matriz: matriz[i][j] = 1.
        4. Se nao_direcionado=True, também marcar a conexão inversa matriz[j][i] = 1.
        """

        if origem not in self.vertices or destino not in self.vertices:
            print("Um dos vértices não existe.")
            return
        
        i = self.vertices.index(origem)
        j = self.vertices.index(destino)

        self.matriz[i][j] = 1
        if nao_direcionado:       
            self.matriz[j][i] = 1
        print(f"Aresta de '{origem}' para '{destino}' inserida.")

    def remover_vertice(self, vertice):
        """
        Remove um vértice e todas as arestas associadas.

        Passos:
        1. Verificar se o vértice existe em 'vertices'.
        2. Caso exista:
            - Descobrir o índice correspondente (usando vertices.index(vertice)).
            - Remover a linha da matriz na posição desse índice.
            - Remover a coluna (mesmo índice) de todas as outras linhas.
            - Remover o vértice da lista 'vertices'.
        """
        if vertice not in self.vertices:
            print(f"Vértice '{vertice}' não existe.")
            return
        
        index = self.vertices.index(vertice)

        self.matriz.pop(index)
        for linha in self.matriz:
            linha.pop(index)
        
        self.vertices.remove(vertice)

        return(f"Vértice '{vertice}' removido com sucesso")

    def remover_aresta(self, origem, destino, nao_direcionado=False):
        """
        Remove uma aresta entre dois vértices.
    
        Passos:
        1. Verificar se ambos os vértices existem.
        2. Localizar os índices (i e j).
        3. Remover a aresta: matriz[i][j] = 0.
        4. Se nao_direcionado=True, também remover a inversa: matriz[j][i] = 0.
        """
        if origem not in self.vertices or destino not in self.vertices:
            print("Um dos vertices não existe")
            return
        
        indexes = self.indentificar_index(origem, destino)
        index_origem = indexes[origem]
        index_destino = indexes[destino]

        self.matriz[index_origem][index_destino] = 0
        if nao_direcionado:
            self.matriz[index_destino][index_origem] = 0
        print(f"Aresta de '{origem}' para '{destino}' removida.")
    
    def existe_aresta(self, origem, destino):
        """
        Verifica se existe uma aresta direta entre dois vértices.
    
        Passos:
        1. Verificar se ambos os vértices existem em 'vertices'.
        2. Obter os índices (i, j).
        3. Retornar True se matriz[i][j] == 1, caso contrário False.
        """
        if origem not in self.vertices or destino not in self.vertices:
            return False
        
        indexes = self.indentificar_index(origem, destino)
        index_origem = indexes[origem]
        index_destino = indexes[destino]

        if self.matriz[index_origem][index_destino] == 1:
            return True
        else:
            return False
    
    def vizinhos(self, vertice):
        """
        Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').
    
        Passos:
        1. Verificar se 'vertice' existe em 'vertices'.
        2. Obter o índice 'i' correspondente.
        3. Criar uma lista de vizinhos vazia
        4. Para cada item da linha matriz[i], verificar se == 1
            - Adicionar o vértice correspondente na lista de vizinhos
        5. Retornar essa lista.
        """
        if vertice not in self.vertices:
            print(f"Vértice '{vertice}' não existe.")
            return []
        
        index_coluna = 0
        index = self.indentificar_index(vertice)[vertice]
        vizinhos = []
        for coluna in self.matriz[index]:
            if coluna == 1:
                vizinhos.append(self.vertices[index_coluna])
            
            index_coluna += 1
        
        return vizinhos
    
    def grau_vertices(self):
        """
        Calcula o grau de entrada, saída e total de cada vértice.
    
        Passos:
        1. Criar um dicionário vazio 'graus'.
        2. Para cada vértice i:
            - Se o grafo for direcionado:
                - Grau de saída: somar os valores da linha i.
                - Grau de entrada: somar os valores da coluna i.
                - Grau total = entrada + saída.
            - Se não:
                - calcular apenas o grau de saida ou entrada
        3. Armazenar no dicionário no formato:
            graus[vértice] = {"saida": x, "entrada": y, "total": z} ou graus[vértice] = x.
        4. Retornar 'graus'.
        """
        graus = {}
        for v in self.vertices:
            i = self.vertices.index(v)
            saida = sum(self.matriz[i])
            entrada = sum(linha[i] for linha in self.matriz)
            total = entrada + saida
            graus[v] = {"saida": saida, "entrada": entrada, "total": total}
        
        return graus
    
    
    def percurso_valido(self, caminho):
        """
        Verifica se um percurso (sequência de vértices) é possível no grafo.
    
        Passos:
        1. Percorrer a lista 'caminho' de forma sequencial (de 0 até len-2).
        2. Para cada par consecutivo (u, v):
            - Verificar se existe_aresta(matriz, vertices, u, v) é True.
            - Se alguma não existir, retornar False.
        3. Se todas existirem, retornar True.
        """
        for i in range(len(caminho) - 1):
            origem, destino = caminho[i], caminho[i + 1]
            if not self.existe_aresta(origem, destino):
                print(f"Não existe aresta de '{origem}' para '{destino}'. Percurso inválido.")
                return False
        print("Percurso válido!")
        
        return True
    
    def listar_vizinhos(self, vertice):
        """
        Exibe (ou retorna) os vizinhos de um vértice.
    
        Passos:
        1. Verificar se o vértice existe.
        2. Chamar a função vizinhos() para obter a lista.
        3. Exibir a lista formatada (ex: print(f"Vizinhos de {v}: {lista}")).
        """
        viz = self.vizinhos(vertice)

        if viz:
            print(f"Vizinhos de '{vertice}': {', '.join(viz)}")
        else:
            print(f"Vértice '{vertice}' não possui vizinhos ou não existe.")
    
    def exibir_grafo(self):
        """
        Exibe o grafo em formato de matriz de adjacência.
    
        Passos:
        1. Exibir cabeçalho com o nome dos vértices.
        2. Para cada linha i:
            - Mostrar o nome do vértice.
            - Mostrar os valores da linha (0 ou 1) separados por espaço.
        """
        print("\nMatriz de Adjacência:")
        print("   ", " ".join(self.vertices))
        for i, v in enumerate(self.vertices):
            linha = " ".join(str(x) for x in self.matriz[i])
            print(f"{v}: {linha}")
        print()

grafo = Grafo()

grafo.inserir_vertice("A")
grafo.inserir_vertice("B")
grafo.inserir_vertice("C") 

grafo.inserir_aresta("A", "B")
grafo.inserir_aresta("B", "C")
grafo.inserir_aresta("A", "C")

grafo.exibir_grafo()
grafo.listar_vizinhos("A")

print("\nGrau dos Vértices: ")
for v, info in grafo.grau_vertices().items():
    print(f"{v}: {info}")

grafo.percurso_valido(["A", "B", "C"])
grafo.percurso_valido(["C", "A"])