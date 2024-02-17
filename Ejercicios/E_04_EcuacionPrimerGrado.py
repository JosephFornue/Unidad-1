import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_04_EcuacionPrimerGrado.ui"  # Nombre del archivo aquí.
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
        m = int(self.txt_m_2.text())
        x = int(self.txt_x_2.text())
        b = int(self.txt_b_2.text())
        result = (m*x) + b
        cadena = "El resultado es: "+str(result)

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())