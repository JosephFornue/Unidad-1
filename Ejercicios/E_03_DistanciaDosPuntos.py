import sys
from PyQt5 import uic, QtWidgets
import math

qtCreatorFile = "E_03_DistanciaDosPuntos.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_distancia)

    # Área de los Slots
    def calcular_distancia(self):
        x1 = float(self.txt_x1.text())
        y1 = float(self.txt_y1.text())
        x2 = float(self.txt_x2.text())
        y2 = float(self.txt_y2.text())

        distancia = self.calcular_distancia_euclidiana(x1, y1, x2, y2)

        cadena = "La distancia entre los dos puntos es: "+str(distancia)

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

    def calcular_distancia_euclidiana(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

