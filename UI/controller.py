import flet as ft
from geopy import distance

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        anni = DAO.getYears()
        for anno in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(anno))
        forme = DAO.getForma()
        for forma in forme:
            self._view.ddshape.options.append(ft.dropdown.Option(forma))
        self._view.update_page()
        pass

    def handle_graph(self, e):
        stati = DAO.getState()
        y = self._view.ddyear.value
        s = self._view.ddshape.value
        self._model.creaGrafo(stati,y,s)
        self._view.txt_result.controls.append(ft.Text(self._model.stampa()))
        self._view.update_page()
        pass
    def handle_path(self, e):
        path,w = self._model.findPath()
        self._view.txtOut2.controls.append(ft.Text(f"Peso cammino massimo: {w}"))
        for i in range(len(path)-1):
            self._view.txtOut2.controls.append(ft.Text(f"{path[i]}-->{path[i+1]}: weight = {self._model.grafo[path[i]][path[i+1]]["weight"]} , distance = {distance.geodesic((path[i].lat,path[i].lon),(path[i+1].lat,path[i+1].lon))}"))
        self._view.update_page()
        pass