from PyQt5 import QtWidgets, QtGui, uic


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.canvas.setPixmap(QtGui.QPixmap())
        self.do_paint = False
        self.newCircle.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        pen = QtGui.QPen(QtGui.QColor(255, 255, 0))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        qp.setPen(pen)
        qp.setBrush(brush)
        size = __import__("random").randint(100, 300)
        qp.drawEllipse(__import__("random").randint(0, 960), __import__("random").randint(0, 510), size, size)


if __name__ == '__main__':
    app = QtWidgets.QApplication(__import__("sys").argv)
    ex = Main()
    ex.show()
    __import__("sys").exit(app.exec_())