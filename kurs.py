# python version    is 3.8.9
# networkx version  is 2.8.4
# Код для отслеживания зависимости среднего количества различных доминирующих множеств от вероятности появления ребра
import networkx as nx
import random as rand


def subsets_of_set(main_set):
    arr_of_subsets=[[]]
    for x in main_set:
        for i in range(len(arr_of_subsets)):
            tmp_list = arr_of_subsets[i].copy()
            tmp_list.append(x)
            arr_of_subsets.append(tmp_list)
    for i in range(len(arr_of_subsets)):
        if arr_of_subsets[i] != []:
            arr_of_subsets[i] = set(arr_of_subsets[i])
        else:
            arr_of_subsets[i] = {}
    return arr_of_subsets


def generate_random_edges(G, V, probability):
    for i in range(1, len(V)):
        for j in range(i+1, len(V)+1):
            if rand.randint(1,100) <= probability:
                G.add_edge(i, j)
    return G


vertices = {1,2,3,4,5,6,7,8,9,10}
subsets = subsets_of_set(list(vertices))
domin_array = [0 for i in range(101)]
for i in range(0, 101):
    print(f"probability = {i}%")
    probability = i
    for j in range(0, 1000):
        G = nx.Graph()
        G.add_nodes_from(vertices)
        G = generate_random_edges(G.copy(), list(vertices.copy()), probability)

        domin_counter = 0
        counter = 0
        for k in range(len(subsets)):
            counter += 1
            if nx.is_dominating_set(G, subsets[k]):
                domin_counter += 1
        domin_array[i] += domin_counter
    
    domin_array[i] /= 1000
    print("average number of dominating sets =", domin_array[i])
    print()
