import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_06_PromedioCalificaciones.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_promedio.clicked.connect(self.calcularPromedio)

    # Área de los Slots
    def calcularPromedio(self):
        calif1 = float(self.txt_c1.text())
        calif2 = float(self.txt_c2.text())
        calif3 = float(self.txt_c3.text())
        calif4 = float(self.txt_c4.text())
        calif5 = float(self.txt_c5.text())
        prom = (calif1+calif2+calif3+calif4+calif5)/5

        cadena = "El promedio es: "+str(prom)


        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())