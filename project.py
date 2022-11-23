#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import networkx as nx
from matplotlib import pyplot as plt


# In[2]:


def labelMaker(n):
    labels = {i+1: f'Node {i+1}' for i in range(n)}
    return labels

def drawMyGraph(graph):
    n = len(graph.keys())
    G = nx.from_dict_of_dicts(graph, create_using=nx.DiGraph)
    pos = nx.spiral_layout(G)
    labels = labelMaker(n)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos, labels)
    nx.draw_networkx_edges(G, pos)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.tight_layout()
    plt.show()


# In[3]:


def adj_to_graph(adj_matrix):
    adj_matrix = np.array(adj_matrix)
    rows, cols = adj_matrix.shape
    
    # node_number_to_alphabet = {0 : 'A',1 : 'B',2 : 'C',3 : 'D',4 : 'E',5 : 'F',6 : 'G',7 : 'H',8 : 'I',9 : 'J',10 : 'K',11 : 'L',12 : 'M',13 : 'N',14 : 'O',15 : 'P',16 : 'Q',17 : 'R',18 : 'S',19 : 'T',20 : 'U',21 : 'V',22 : 'W',23 : 'X',24 : 'Y',25 : 'Z',}
    graph = {}
    for i in range(rows):
        destinations = {}
        for j in range(cols):
            if adj_matrix[i][j] != 0:
                destinations[j+1] = {'weight' : adj_matrix[i][j]} # adding 1 to index label to label nodes with 1-indexing
        graph[i+1] = destinations # adding 1 to index label to label nodes with 1-indexing
        # destinations[node_number_to_alphabet[j]] = {'weight' : adj_matrix[i][j]}
        # graph[node_number_to_alphabet[i]] = destinations

    return graph


# In[4]:


def bellmanford(graph,src,dest):
    inf = np.inf
    node_data={}
    for i in graph.keys():
        a={i:{"cost":inf,"pred":[]}}
        node_data.update(a)
    # print(node_data)
    
    node_data[src]['cost'] = 0
    
    for i in range(len(node_data.keys())):
        for itr in graph:
            for neighbor in graph[itr]:
                for weight in graph[itr][neighbor]:
                    cost = node_data[itr]['cost'] + graph[itr][neighbor][weight]
                    if cost < node_data[neighbor]['cost']:
                        node_data[neighbor]['cost'] = cost
                        if node_data[neighbor]['cost']== inf:
                            node_data[neighbor]['pred'] = node_data[itr]['pred'] + [itr]
                        else:
                            node_data[neighbor]['pred'].clear()
                            node_data[neighbor]['pred'] = node_data[itr]['pred'] + [itr]
    # print(node_data)
    
    '''print(node_data)
    if node_data[dest]['cost'] == inf:
        print("Path cost = inf, impossible path")
    else:
        print("Shortest Distance Cost : " + str(node_data[dest]['cost']))
        print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))
    '''
    return node_data[dest]['cost'], node_data[dest]['pred']+[dest]
  


# In[5]:


def belaman_evaluation(graph):
    node_list = graph.keys()
    print('Source-Destination\t|\tCost\t|\tPath')
    print('-'*100)
    # for i in node_list:
    source=1
    for j in node_list:    
        destination=j
        cost, path = bellmanford(graph,source,destination)
        if cost!= np.inf:
            print(f'{source}-{destination}\t\t\t|\t{cost}\t|\t{path}')
            print('-'*100)
            


# In[7]:


A_cycle = np.array([
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],])


graph_cycle = adj_to_graph(A_cycle)
#print(graph_cycle)
drawMyGraph(graph= graph_cycle)


belaman_evaluation(graph_cycle)


#  # FOR CYCLE GRAPH

# In[9]:


A_cycle = np.array([
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],])


graph_cycle = adj_to_graph(A_cycle)
#print(graph_cycle)
drawMyGraph(graph= graph_cycle)


belaman_evaluation(graph_cycle)


# # FOR PATH GRAPH

# In[10]:


A_path = np.array([
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],])


graph_path = adj_to_graph(A_path)
#print(graph_cycle)
drawMyGraph(graph= graph_path)


belaman_evaluation(graph_path)


# # FOR STAR GRAPH

# In[14]:


A_star = np.array([
    [0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],])


graph_star = adj_to_graph(A_star)
#print(graph_cycle)
drawMyGraph(graph= graph_star)

belaman_evaluation(graph_star)


# # FOR BIPARTITE GRAPH

# In[16]:


A_bipartite = np.array([
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],])


graph_bipartite = adj_to_graph(A_bipartite)
#print(graph_cycle)

belaman_evaluation(graph_bipartite)


# # FOR COMPLETE GRAPH

# In[17]:


A_complete = np.array([
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0],])


graph_complete = adj_to_graph(A_complete)
#print(graph_cycle)

belaman_evaluation(graph_complete)


# # FOR NEGATIVE GRAPH

# In[18]:


A_negative = np.array([
        [ 0,  6,  4,  5,  0,  0],
        [ 0,  0,  0,  0, -1,  0],
        [ 0, -2,  0,  0,  3,  0],
        [ 0,  0, -2,  0,  0, -1],
        [ 0,  0,  0,  0,  0,  3],
        [ 0,  0,  0,  0,  0,  0]
        ])

graph_negative = adj_to_graph(A_negative)

belaman_evaluation(graph_negative)


# In[19]:


def create_component_matrix(random_matrix):
    shape = np.shape(random_matrix)
    k = shape[0]
    component_matrix=[]
    for i in range(k):
        zero_matrix = np.zeros(k)
        while True:
            array = np.random.choice(k,2)
            a,b = array
            if a != b and a != i and b != i:
                break
        for j in array:
            zero_matrix[j] = 1
        component_matrix.append(zero_matrix)
    new_matrix = np.array(component_matrix)
    print(new_matrix)
    return  new_matrix * random_matrix
    




# # FULLY CONNECTED GRAPH

# In[20]:


random_matrix = np.array([
        [ 1,  6,  4,  5,  4,  3],
        [ 7,  8,  9,  6, -1,  2],
        [ 1, -2,  2,  1,  3,  4],
        [ 7,  8, -2,  3,  2, -1],
        [ 2,  1,  3,  5,  4,  3],
        [ 1,  2,  3,  4,  5,  6]
        ])
adjacency_matrix  = create_component_matrix(random_matrix)
# adjacency_matrix = component_matrix * random_matrix

graph = adj_to_graph(adjacency_matrix)
drawMyGraph(graph= graph)

belaman_evaluation(graph)


# In[ ]:




