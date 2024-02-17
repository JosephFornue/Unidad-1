import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_02_DeterminarIMC.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_IMC.clicked.connect(self.calcularIMC)

    # Área de los Slots
    def calcularIMC(self):
        try:
            peso = float(self.txt_peso.text())
            altura = float(self.txt_altura.text())

            # Validar que la altura sea un número decimal positivo
            if not 0 < altura < 10:  # Puedes ajustar el rango según tus necesidades
                raise ValueError("La altura debe ser un número decimal positivo y real.")

            IMC = peso / (altura * altura)
            IMCredondeado = round(IMC, 2)
            cadena = "Tu IMC es: " + str(IMCredondeado)

            msj = QtWidgets.QMessageBox()
            msj.setText(cadena)
            msj.exec_()

        except ValueError as error:
            msj_error = QtWidgets.QMessageBox()
            msj_error.setText("Error: " + str(error))
            msj_error.setIcon(QtWidgets.QMessageBox.Warning)
            msj_error.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
