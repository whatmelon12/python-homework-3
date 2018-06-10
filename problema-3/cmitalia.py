import csv
import numpy as np
import scipy.sparse.csgraph as csgraph
import matplotlib.pyplot as plt
import networkx as nx

def LoadData():
    data = []
    with open('italian_cities.csv', 'r') as f:
        try:
            data = list(csv.reader(f, delimiter=','))[1:]
        except Exception as e:
            print(e)
        finally:
            f.close()
    return np.array(data).astype(np.int)

def CreateGraph(data):
    n = len(data)
    G = nx.Graph()
    nx.path_graph(n, G)

    for row in range(n):
        for column in range(n):
            weight = data[row][column]
            if(weight != 0):
                G.add_edge(row, column, weight= weight)
    return G

def main():
    data = LoadData()
    dijkstra = csgraph.shortest_path(data, method='D')
    floyd_warshall = csgraph.shortest_path(data, method='FW')

    #Impresion del calculo
    # print(data)
    print('\nDijkstra shortest path result:')
    print(dijkstra)
    print('\nFloyd-Warshall shortest path result:')
    print(floyd_warshall)

    #Impresion del grafo
    cities = CreateGraph(data) 
    nx.draw(cities, with_labels=True, font_weight='bold')   
    #nx.draw_networkx_edge_labels(cities, pos=nx.spring_layout(cities))    
    plt.show()

if __name__ == '__main__':
    main()