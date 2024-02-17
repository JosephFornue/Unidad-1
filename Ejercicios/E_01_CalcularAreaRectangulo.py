import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_01_CalcularAreaRectangulo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    
        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        longitud = float(self.txt1.text())
        ancho = float(self.txt2.text())
        area = longitud*ancho

        msj = QtWidgets.QMessageBox()
        msj.setText("El area del rectangulo es: " + str(area))
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
