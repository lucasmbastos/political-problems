import numpy as np
import math
import resource
import random
import sys
import os
import time
import matplotlib.pyplot as plt

info = resource.getrusage(resource.RUSAGE_CHILDREN)

i = 0
num_vertices = 150
num_edges = []
tempo_edges = []
# for x in np.arange(1, 6, 0.4):
for x in np.arange(0, 1.1, 0.1):
    print("{}: {}".format(i, x))
    #criar_arquivo
    arquivo_nome = "tests/teste{}.txt".format(i)
    entrada = open(arquivo_nome, 'w')
    nodes = list(range(num_vertices))
    nodes2 = nodes.copy()
    for y in nodes:
        nodes2.remove(y)
        for z in nodes2:
            if random.uniform(0,1) < x:
                peso = math.ceil(random.uniform(0,1) * 100)
                entrada.write("{},{},{}\n".format(y,z,peso))

    entrada.write("0,0,0\n")
    entrada.close()
    #executar 
    start = time.time()
    os.system(" ".join(["./executar.sh", arquivo_nome, "tests/dummy.out"]))
    num_edges.append(x)
    tempo_edges.append(time.time() - start)

    #salvar tempo
    i+=1

plt.plot(num_edges, tempo_edges)
plt.ylabel("Tempo de execução (em segundos)")
plt.xlabel("Probabilidade dos nós possuírem uma aresta")
plt.title("Relação de tempo com número de arestas")
plt.show()