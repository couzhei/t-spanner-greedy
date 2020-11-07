#!/usr/bin/python python=3.8
# Created at datetime.datetime(2020, 11, 7, 20, 42, 18, 929057)
# by couzhei

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDoubleSpinBox, QLabel, QMessageBox
import sys
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from digraph.graph import WeightedGraph
from digraph.points import Point
from digraph.graph_algorithms import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Greedy t-Spanner implementation using PyQt5"
        top = 400
        left = 400
        width = 604
        height = 450
        self.t = 1.01

        self.canvas = Canvas(self, width=6, height=4)
        self.canvas.move(2, 2)
        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.my_ui()

    def my_ui(self):

        x, y = 325, 410

        spinbox_label = QLabel("Stretch Factor (t):", self)
        spinbox_label.setGeometry(x - 300, y, 135, 30)

        self.spinbox = QDoubleSpinBox(self)
        self.spinbox.setGeometry(x - 190, y, 50, 30)
        self.spinbox.setMinimum(1.01)
        self.spinbox.setSingleStep(0.01)
        self.spinbox.valueChanged.connect(self.set_t)

        button3 = QPushButton("Perform", self)
        button3.setGeometry(x - 110, y, 50, 30)
        button3.clicked.connect(self.perform)

        button4 = QPushButton("Draw", self)
        button4.setGeometry(x - 50, y, 40, 30)
        button4.clicked.connect(self.draw)

        button = QPushButton("Save your Graph", self)
        button.setGeometry(x, y, 108, 30)
        button.clicked.connect(self.save)

        button2 = QPushButton("Load previous Graph", self)
        button2.setGeometry(x + 120, y, 135, 30)
        button2.clicked.connect(self.load)

    def perform(self):
        try:
            self.canvas.mpl_disconnect(cid=self.cid)
        except:
            pass
        finally:
            if len(points) < 2:
                return None
            # ---------------------------------------------------------------------------------------- #
            #  The algorithm goes here                                                                 #
            # ---------------------------------------------------------------------------------------- #
            G = WeightedGraph(points)
            unordered_edges = set()

            for fixed_point in points:
                for next_point in points:
                    if fixed_point == next_point:
                        continue
                    edge = UndirectedEdge(fixed_point, next_point)
                    unordered_edges.add(edge)

            L = sorted(list(unordered_edges), key=lambda x: x.getWeight())
            for edge in L:
                dist = edge.getWeight()
                delta = shortest_path(G, edge.getSource(), edge.getDestination())
                if self.t * dist < delta:
                    G.addEdge(edge)

            #  Now showing the graph
            self.plot(G)
            # self.canvas.figure.clf()
            # self.canvas.clear()

    def set_t(self):
        self.t = self.spinbox.value()

    def draw(self):
        global points
        if points:
            txt = "Click Yes if you want to continue adding points, otherwise to start fresh, click No."
            check_clear = QMessageBox(self)
            check_clear.setIcon(QMessageBox.Information)
            check_clear.setWindowTitle("Warning")
            check_clear.setText(txt)
            check_clear.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button = check_clear.exec_()
            if button == QMessageBox.Yes:
                self.cid = self.canvas.mpl_connect('button_press_event', self.onclick)
            else:
                points = list()
                self.canvas.clear()
                self.canvas = Canvas(self, width=6, height=4)
                self.canvas.move(2, 2)
                self.canvas.show()
                self.draw()

        else:
            self.cid = self.canvas.mpl_connect('button_press_event', self.onclick)

    def save(self):
        try:
            self.canvas.mpl_disconnect(cid=self.cid)
        except:
            pass
        finally:
            if os.path.isfile("save.txt"):
                os.remove("save.txt")
            if points:
                with open("save.txt", "w") as fh:
                    saved_document = "["
                    for point in points:
                        saved_document += f"Point({point.getX()}, {point.getY()}),\n"
                    saved_document = saved_document[:-2] + "]"
                    fh.write(saved_document)
                    fh.close()
                message_box = QMessageBox(self)
                message_box.about(self, "Warning", "Successfully saved your points.")
            else:
                message_box = QMessageBox(self)
                # image = QImage()
                # image.loadFromData(os.path("warning.png"))
                # pixmap = QPixmap(image).scaledToHeight(32, Qt.SmoothTransformation)
                # message_box.setIconPixmap(pixmap)
                # message_box.setWindowIcon(QIcon("warning.png"))
                message_box.about(self, "Warning", "There's nothing to be saved")

    def load(self):
        try:
            self.canvas.mpl_disconnect(cid=self.cid)
        except:
            pass
        finally:
            if os.path.isfile("save.txt"):
                with open("save.txt", "r") as fh:
                    global points
                    points = eval(fh.read())
                    fh.close()
                self.plot(WeightedGraph(points))
            else:
                message_box = QMessageBox(self)
                message_box.about(self, "Warning", "There's nothing to be loaded")

    def onclick(self, event):
        """It's an event handler, in this case, clicking on the plot"""
        points.append(Point(event.xdata, event.ydata))
        self.canvas.axes.plot(event.xdata, event.ydata, "o")
        self.canvas.draw()

    def clear(self):
        self.canvas.clear()
        global points
        points = []
        self.draw()

    def plot(self, graph):
        self.canvas = Canvas(self, width=6, height=4)
        self.canvas.move(2, 2)

        pts = graph.getNodes()
        lines = graph.getEdges()

        for line in lines:
            x1, x2 = line.getSource().getX(), line.getDestination().getX()
            y1, y2 = line.getSource().getY(), line.getDestination().getY()
            self.canvas.axes.plot([x1, x2], [y1, y2], 'go-')

        for pt in pts:
            self.canvas.axes.plot(pt.getX(), pt.getY(), 'ro')
            self.canvas.axes.axis('equal')

        self.canvas.show()


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=9, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_xlim([-10, 10])
        self.axes.set_ylim([-10, 10])
        # ax.set_xlim([-10, 10])
        # ax.set_ylim([-10, 10])

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        # self.mpl_connect()

        # self.plot()

    def clear(self):
        self.__init__()


global points
points = []
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
