import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_05_CalcularPuntoMedio.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcularEc)

    # Área de los Slots
    def calcularEc(self):
        x1 = float(self.txt_x1.text())
        y1 = float(self.txt_y1.text())
        x2 = float(self.txt_x2.text())
        y2 = float(self.txt_y2.text())

        punto_medio_x = (x1 + x2) / 2
        punto_medio_y = (y1 + y2) / 2

        cadena = ("El punto medio entre: "+"("+str(x1)+","+str(y1)+") y ("+str(x2)+","+str(y2)+") es: ("+str(punto_medio_x)+","+str(punto_medio_y)+")")

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())