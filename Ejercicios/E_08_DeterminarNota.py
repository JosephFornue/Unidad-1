import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_08_DeterminarNota.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        cadena = ""
        self.btn_calcularNota.clicked.connect(self.calcular)
    # Área de los Slots
    def calcular(self):
        alumno = self.txt_nombre.text()
        calificacion = int(self.txt_calif.text())

        if calificacion == 10:
            nota = "A"
        elif calificacion == 9:
            nota = "B"
        elif calificacion == 8:
            nota = "C"
        elif calificacion == 7:
            nota = "D"
        elif calificacion == 6:
            nota = "E"
        else:
            nota = "F"

        cadena = "La nota del alumno: " +alumno+ " = "+nota

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
