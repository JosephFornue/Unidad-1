import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_07_FactorialNumero.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_factorial)

    # Área de los Slots
    def calcular_factorial(self):
        numero = int(self.txt_factorial.text())
        resultado = self.factorial(numero)

        cadena = "el numero en factorial es: "+str(resultado)

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

    def factorial(self, n):
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
