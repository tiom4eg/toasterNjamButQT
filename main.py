from PyQt5 import QtWidgets, QtGui, uic

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(989, 571)
        self.canvas = QtWidgets.QLabel(Form)
        self.canvas.setGeometry(QtCore.QRect(14, 15, 961, 511))
        self.canvas.setText("")
        self.canvas.setObjectName("canvas")
        self.newCircle = QtWidgets.QPushButton(Form)
        self.newCircle.setGeometry(QtCore.QRect(870, 540, 93, 28))
        self.newCircle.setObjectName("newCircle")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.newCircle.setText(_translate("Form", "create circle"))


class Main(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        color = QtGui.QColor(__import__("random").randint(0, 255), __import__("random").randint(0, 255), __import__("random").randint(0, 255))
        pen = QtGui.QPen(color)
        brush = QtGui.QBrush(color)
        qp.setPen(pen)
        qp.setBrush(brush)
        size = __import__("random").randint(100, 300)
        qp.drawEllipse(__import__("random").randint(0, 960), __import__("random").randint(0, 510), size, size)


if __name__ == '__main__':
    app = QtWidgets.QApplication(__import__("sys").argv)
    ex = Main()
    ex.show()
    __import__("sys").exit(app.exec_())