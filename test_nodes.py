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
treshold = 0.1
num_vertices = []
tempo_vertices = []
# for x in np.arange(1, 6, 0.4):
for x in np.arange(1, 9, 0.4):
    valor_formula = math.ceil(2 ** x)
    print("Executando {}: valor_formula: {}\n".format(i, valor_formula))
    #criar_arquivo
    arquivo_nome = "tests/test{}.txt".format(i)
    entrada = open(arquivo_nome, 'w')
    nodes = list(range(valor_formula))
    nodes2 = nodes.copy()
    for y in nodes:
        nodes2.remove(y)
        for z in nodes2:
            if random.uniform(0,1) < treshold:
                peso = math.ceil(random.uniform(0,1) * 100)
                entrada.write("{},{},{}\n".format(y,z,peso))

    entrada.write("0,0,0\n")
    entrada.close()
    #executar 
    start = time.time()
    os.system(" ".join(["./executar.sh", arquivo_nome, "tests/dummy.out"]))
    num_vertices.append(valor_formula)
    tempo_vertices.append(time.time() - start)

    #salvar tempo
    i+=1

plt.plot(num_vertices, tempo_vertices)
plt.ylabel("Tempo de execução (em segundos)")
plt.xlabel("Número de Vértices")
plt.title("Relação de tempo com número de vértices")
plt.show()