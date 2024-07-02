import copy

import networkx as nx
from geopy import distance
from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def creaGrafo(self, stati, y, sh):
        self.nodi = stati
        self.idMap = {}
        for s in stati:
            self.idMap[s.id] = s
        self.grafo = nx.Graph()
        self.grafo.add_nodes_from(self.nodi)
        self.grafo.add_edges_from(DAO.getNeig(self.idMap))
        for e in self.grafo.edges:
            self.grafo[e[0]][e[1]]["weight"] = DAO.getPeso(y, sh, e[0].id, e[1].id)

    def stampa(self):
        stringa = ""
        for nodo in self.grafo.nodes:
            peso = 0
            for nei in self.grafo.neighbors(nodo):
                peso += self.grafo[nodo][nei]["weight"]
            stringa += f"{nodo.id} somma pesi = {peso}\n"
        return (f"Numero nodi:{len(self.grafo.nodes)}, numero archi: {len(self.grafo.edges)}\n {stringa}")

    def findPath(self):
        self.bestPath = []
        self.maxDist = 0
        for n in self.nodi:
            self.ricorsione([n])
        return self.bestPath, self.maxDist




